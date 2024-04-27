from checkTokens import *
from createCsv import *
from transitionTable import *
from checkWords import *

def main():
    check = checkTokens()

    identifiers = [[]]
    identifiersNum = 0

    digits = [[]]
    digitsNum = 0

    delimitadores = [
        ':', ';', '(', ')'
        '[', ']', '{', '}'
    ]

    tokens = [[]]
    tokensNum = 0


    with open('code.txt','r') as file:   
        for line in file:
            word = ""
            ubicacion = 0
            for char in line:
                print("Tokens", tokens)
                print("Tokens Identifier", identifiers)
                print("Tokens Digits", digits)
                char = char.lower()
                if ubicacion != -1:
                    ubicacion = checkTransitionTable(char, ubicacion)
                    # print("Ubicacion: ", ubicacion)
                    # print("Char: ", char)
                    if ubicacion <= 11:
                        word = word + char 
                        # print("Word in <= 11: ",  word)                       
                if ubicacion >= 11:
                    # print("Word: ", word)
                    if word != "":
                        if checkWord(word) is True:
                            #CHECA EL NUMERO DEL TOKEN DE LA PALABRA
                            numToken = check.readToken(word)

                            #AÑADE EL TOKEN A LA LISTA
                            tokens[tokensNum].append('< ' + str(numToken) + ' >')
                            tokensNum = tokensNum + 1

                            #UBICACION DEL NUEVO CHAR
                            ubicacion = checkTransitionTable(char, 0)
                            word = char 
                        
                        #CHECA SI WORD EMPIEZA PRIMERO CON {
                        elif checkSingleComment(word) == '{':
                            
                            #REGRESA EL TOKEN DE {
                            numToken = check.readToken('{')
                            
                            #AÑADE EL TOKEN A LA LISTA
                            tokens[tokensNum].append('< ' + str(numToken) + ' >')
                            tokensNum = tokensNum + 1

                            #UBICACION DEL NUEVO CHAR
                            ubicacion = checkTransitionTable(char, 0)
                            word = char

                            #CHECA SI LA UBICACION ES MAYOR A 11
                            if ubicacion >= 11:
                                if checkWord(word) is True:
                                    
                                    #REGRESA EL NUMERO DEL TOKEN
                                    numToken = check.readToken(word)

                                    #AÑADE EL NUMERO A LA LISTA DE TOKENS
                                    tokens[tokensNum].append('< ' + str(numToken) + ' >')
                                    tokensNum = tokensNum + 1
                                    ubicacion = 0
                                    word = ""

                        # elif checkMultipleComment(word) ==
                        elif checkDigit(word) is True:

                            #CHECA SI EL DIGITO ESTA REGISTRADO EN LA LISTA DE DIGITOS
                            if word in digits:
                                
                                #REGRESA EL NUMERO DEL TOKEN
                                numToken = check.readToken('digit')
                                
                                #AÑADE EL NUMERO A LA LISTA DE TOKENS
                                tokens[tokensNum].append('< ' + str(numToken) + ' , '+ str(digitsNum) + ' >')
                                

                                #AÑADE EL NUMERO A LA LISTA DE TOKENS DE DIGITOS
                                digits[digitsNum].append([str(digitsNum), word])
                
                                digitsNum = digitsNum + 1
                                tokensNum = tokensNum + 1

                                ubicacion = checkTransitionTable(char, 0)
                                word = char
                                if ubicacion >= 11:
                                    if checkWord(word) is True:
                                        # print("Word: ", word)
                                        numToken = check.readToken('{')

                                        tokens[tokensNum].append('< ' + str(numToken) + ' >')
                                        tokensNum = tokensNum + 1

                                        ubicacion = 0
                                        word = ""

                        elif checkDigit(word) is False:
                            # print("< " + str(identifiersNum) + " , " + str(word) + " >")
                            
                            #CHECA SI WORD ESTA EN LA LISTA DE IDENTIFICADORES
                            if word in identifiers:

                                #OBTIENE EL TOKEN DEL IDENTIFICADOR
                                numToken = check.readToken('identifier')
                                print(numToken)
                                #AÑADE EL TOKEN A LA LISTA DE TOKENS
                                tokens[tokensNum].append('< ' + str(numToken) + ' , '+ str(digitsNum) + ' >')

                                #AÑADE A LOS TOKES A LA LISTA DE TOKES DE IDENTIFICADORES
                                identifiers[identifiersNum].append([str(numToken),word])
                                
                                identifiersNum = identifiersNum + 1
                                tokensNum = tokensNum + 1

                                ubicacion = checkTransitionTable(char, 0)
                                word = char
                                if ubicacion >= 11:
                                    # print("Word: ", word)
                                    if checkWord(word) is True:
                                        # print("Word: ", word)
                                        numToken = check.readToken(word)

                                        tokens[tokensNum].append('< ' + str(numToken) + ' >')
                                        tokensNum = tokensNum + 1

                                        ubicacion = 0
                                        word = ""
    csvTokens(tokens)
    csvDigitTokens(digits)
    csvIdentifiertokens(identifiers)

                       
                
if __name__ == "__main__":
    main()