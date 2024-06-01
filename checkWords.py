def checkWord(word):

    reserverdWords = [
        'program', 'real', 'repeat', 'procedure',
        'string','until','function','array',
        'for','begin','of','to','end','if',
        'do','var','then','readln','else',
        'writeln','integer',        
    ]
    operadores = [
        '+', '-', '*', '/',
        ':=', '=', '<>', '<',
        '<=', '>=', '>'
    ]
    delimitadores = [
        ':', ';', '(', ')', 
        ',', '[', ']', '.'
    ]
    

    if word in reserverdWords or word in operadores or word in delimitadores:
        return True
    return False

def checkDigit(word):
    return word[0].isdigit()

def checkIntegerReal(word):
    
    
    if "." in word:
        print(word) 
        return False
    return True

def checkSingleComment(word):    
    if word[0] == '{':
        return '{'
    return ''

def checkMultipleComment(word):
    if word[0] == '(' and word[1] == '*':
         return '(*'

def checkString(word):
    if word[0] == "'" and word[-1] == "'":
        return True
    return False

def checkInList(word_list, word):
    for elemento in word_list:
        if word == elemento[1]:
            return elemento
    return None

def continueOperador(word, char):
    operadorContinue = [
        ':=', '<>',
        '<=', '>=',
    ]

    word = word + char

    if word in operadorContinue:
        return True
    return False

def findWordList(word, list):
    for sublist in list[0]:
        if word in sublist:
            return sublist[0]