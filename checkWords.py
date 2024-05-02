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
        ',', '[', ']', 
    ]
    

    if word in reserverdWords or word in operadores or word in delimitadores:
        return True
    return False

def checkDigit(word):
    return word[0].isdigit()

def checkSingleComment(word):    
    if word[0] == '{':
        return '{'
    return ''

# def checkMultipleComment(word):
#     if word[0] == '(' and word[1] == '*':
#         return '(*'

def checkInList(word_list, word):
    for elemento in word_list:
        if word == elemento[1]:
            return elemento
    return None