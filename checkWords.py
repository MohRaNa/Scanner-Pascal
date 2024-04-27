def checkWord(word):

    reserverdWords = [
        'program', 'real', 'repeat', 'procedure',
        'string','until','function','array',
        'for','begin','of','to','end','if',
        'do','var','then','readLn','else',
        'writeLN','integer',        
    ]
    operadores = [
        '+', '-', '*', '/',
        ':=', '=', '<>', '<',
        '<=', '>=', '>'
    ]
    delimitadores = [
        ':', ';', '(', ')'
        '[', ']', '{', '}'
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

