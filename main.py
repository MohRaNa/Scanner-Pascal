from checkTokens import *
from createCsv import *
from transitionTable import *
from checkWords import *

def main():
    check = checkTokens()

    #INICIALIZAR ARRAY DE IDENTIFICADORES
    identifiers = [[]]
    identifiersNum = 1

    #INICIALIZAR ARRAY DE DIGITOS
    digits = [[]]
    digitsNum = 1

    #INICIALIZAR ARRAY DE STRINGS
    strings = [[]]
    stringsNum = 1

    #INICIALIZAR DE TOKENS
    tokens = [[]]
    tokensNum = 0

    saltoDeLinea = False
    operador = False

    # EMPIEZA A LEER EL TXT DEL CODIGO
    with open('code.txt','r') as file:   
        # POR CADA LINEA EN EL ARCHIVO
        for line in file:
            # INICIALIZAR VARIABLES
            word = ""
            ubicacion = 0
            for char in line:

                # QUITA LOS ESPACIOS DE LA PALABRA
                word = word.lstrip()


                #MINIMIZA LOS CARACTERES
                char = char.lower()

                #CHECA SI HAY UN OPERADOR EN LA PALABRA

                operador = continueOperador(word, char) 
                if ubicacion != -1:
                    # MANDA EL CHAR Y LA UBICACION A LA TABLA DE TRANSICIONES
                    ubicacion = checkTransitionTable(char, ubicacion)
                    
                    #CHECA SI LA PALABRA ESTA VACIA Y TIENE UNA UBICACION > 11
                    if word == '' and ubicacion >= 11:
                        word = word + char
                    # CHECA SI LA UBICACION ES MENOR A 11
                    if ubicacion <= 11: 
                        word = word + char
                    #CHECA SI EL NUEVO CHAR ES UN '
                    if word[0] == "'" and char == "'":
                        word = word + char

                # CHECA SI HAY UN OPERADOR
                if operador is True:
                        word = word + char
                        numToken = check.readToken(word)

                        # AÑADE EL TOKEN A LA LISTA
                        tokens[tokensNum].append(['< ' + str(numToken) + ' >'])
                        
                        # EMPEZAR CON NUEVA UBICACION = 0
                        word = ''
                        ubicacion = 0

                # CHECA SI HAY UNA UBICACION MAYOR A 11 Y SI OPERADOR ES FALSO
                if ubicacion >= 11 and operador is False:
                    
                    if word != "":
                        if checkWord(word) is True:
                            # CHECA EL NUMERO DEL TOKEN DE LA PALABRA
                            
                            numToken = check.readToken(word)

                            # AÑADE EL TOKEN A LA LISTA
                            tokens[tokensNum].append(['< ' + str(numToken) + ' >'])
                            

                            # UBICACION DEL NUEVO CHAR EN LA TABLA DE TRANSICIONES
                            ubicacion = checkTransitionTable(char, 0)
                            word = char 

                            #cHECA SI LA NUEVA UBICACION ES MAYOR A 11
                            if ubicacion >= 11:
                                if checkWord(word) is True:
                                    # REGRESA EL NUMERO DEL TOKEN
                                    numToken = check.readToken(word)

                                    # AÑADE EL NUMERO A LA LISTA DE TOKENS
                                    tokens[tokensNum].append(['< ' + str(numToken) + ' >'])
                                    ubicacion = 0
                                    word = ""
                                    saltoDeLinea = False
                        
                        # CHECA SI WORD EMPIEZA PRIMERO CON {
                        elif checkSingleComment(word) == '{':

                            # UBICACION DEL NUEVO CHAR
                            ubicacion = checkTransitionTable(char, 0)
                            word = char
                            saltoDeLinea = False

                            # CHECA SI LA UBICACION ES MAYOR A 11
                            if ubicacion >= 11:
                                if checkWord(word) is True:
                                    
                                    # REGRESA EL NUMERO DEL TOKEN
                                    numToken = check.readToken(word)

                                    # AÑADE EL NUMERO A LA LISTA DE TOKENS
                                    tokens[tokensNum].append(['< ' + str(numToken) + ' >'])
                                    ubicacion = 0
                                    word = ""

                        # elif checkMultipleComment(word) ==
                        elif checkString(word) is True:
                            numToken = check.readToken('string')
                            # AÑADE EL NUMERO A LA LISTA DE TOKENS DE DIGITOS
                            tokens[tokensNum].append(['< ' + str(numToken) +  "," + str(stringsNum) + ' >'])
                            
                            strings[0].append([str(stringsNum), word])
                            # INICIALIZAR EN 0
                            word = ''
                            ubicacion = 0
                        # CHECA SI EL DIGITO ES VERDADERO
                        elif checkDigit(word) is True:
                                # REGRESA EL NUMERO DEL TOKEN
                                if checkIntegerReal(word) is True:
                                    numToken = check.readToken('digit')
                                else:
                                    numToken = check.readToken('realC')
                                
                                # AÑADE EL NUMERO A LA LISTA DE TOKENS
                                tokens[tokensNum].append(['< ' + str(numToken) + ' , '+ str(digitsNum) + ' >'])

                                # AÑADE EL NUMERO A LA LISTA DE TOKENS DE DIGITOS
                                digits[0].append([str(digitsNum), word])
                                digitsNum += 1

                                # CHECA EL SIGUIENTE CARACTER A LA TABLA DE TRANSICION
                                ubicacion = checkTransitionTable(char, 0)
                                word = char
                                saltoDeLinea = False

                                # CHECA SI LA NUEVA UBICACION ES MAYOR A 11
                                if ubicacion >= 11:
                                    if checkWord(word) is True:

                                        numToken = check.readToken(word)

                                        tokens[tokensNum].append(['< ' + str(numToken) + ' >'])

                                        ubicacion = 0
                                        word = ""
                                        saltoDeLinea = False        
                        # CHECA SI ES UN DIGITO, SI NO ES UN IDENTIFICADOR

                        elif checkDigit(word) is False:

                            # OBTIENE EL TOKEN DEL IDENTIFICADOR
                            numToken = check.readToken('identifier')

                            # AÑADE EL TOKEN A LA LISTA DE TOKENS
                            tokens[tokensNum].append(['< ' + str(numToken) + ' , '+ str(identifiersNum) + ' >'])

                            # AÑADE A LOS TOKENS A LA LISTA DE TOKES DE IDENTIFICADORES
                            identifiers[0].append([str(identifiersNum),word])

                            identifiersNum += 1

                            # CHECA EL NUEVO CARACTER EN LA TABLA DE TRANSICION
                            ubicacion = checkTransitionTable(char, 0)
                            word = char
                            
                            #CHECA SI LA NUEVA PALABRA TIENE CONTINUACION,
                            #SI NO HAY CONTINUACION LO AÑADE A LA LISTA DE TOKENS
                            if ubicacion >= 11:
                                # CHECA SI ES UN DELIMITADOR

                                if checkWord(word) is True:
                                    # AGARRA EL NUMERO DE TOKEN
                                    numToken = check.readToken(word)

                                    # LO AÑADE A LA TABLA DE TOKENS
                                    tokens[tokensNum].append(['< ' + str(numToken) + ' >'])

                                    # EMPIEZA DESDE CERO
                                    ubicacion = 0
                                    word = ""
    
    csvTokens(tokens)
    csvDigitTokens(digits)
    csvIdentifiertokens(identifiers)

                       
                
if __name__ == "__main__":
    main()