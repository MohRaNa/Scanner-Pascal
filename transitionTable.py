import sys

def checkTransitionTable(char, ubicacion):

    #Tabla de Transiciones
    transition_table = {
        0: {'Letter': 2, 'Digit': 3, '_': 1, '+': 34, '-': 35, '*': 37, '/': 36,
            '<': 8, '>': 10, '=': 41, ':': 11, ';': 40, ',': 39, "'": 12, '.': 38,
            '(': 6, ')': 20, '[': 42, ']': 43, '{': 7, '}': 58, 'WhiteSpace': 0,
            '\n': 0, 'Symbols': 58},

        1: {'Letter': 2, 'Digit': 57, '_': 57, '+': 57, '-': 57, '*': 57, '/': 57,
            '<': 57, '>': 57, '=': 57, ':': 57, ';': 57, ',': 57, "'": 57, '.': 57,
            '(': 57, ')': 57, '[': 57, ']': 57, '{': 57, '}': 57, 'WhiteSpace': 57,
            '\n': 57, 'Symbols': 57},

        2: {'Letter': 2, 'Digit': 2, '_': 2, '+': 26, '-': 26, '*': 26, '/': 26,
            '<': 26, '>': 26, '=': 26, ':': 15, ';': 15, ',': 15, "'": 44, '.': 44,
            '(': 15, ')': 15, '[': 15, ']': 15, '{': 15, '}': 15, 'WhiteSpace': 15,
            '\n': 15, 'Symbols': 44},

        3: {'Letter': 45, 'Digit': 3, '_': 45, '+': 27, '-': 27, '*': 27, '/': 27,
            '<': 27, '>': 27, '=': 27, ':': 16, ';': 16, ',': 16, "'": 45, '.': 4,
            '(': 16, ')': 16, '[': 16, ']': 16, '{': 16, '}': 16, 'WhiteSpace': 16,
            '\n': 46, 'Symbols': 45},

        4: {'Letter': 47, 'Digit': 5, '_': 47, '+': 47, '-': 47, '*': 47, '/': 47,
            '<': 47, '>': 47, '=': 47, ':': 47, ';': 47, ',': 47, "'": 47, '.': 18,
            '(': 47, ')': 47, '[': 47, ']': 47, '{': 47, '}': 47, 'WhiteSpace': 47,
            '\n': 48, 'Symbols': 47},

        5: {'Letter': 49, 'Digit': 5, '_': 49, '+': 28, '-': 28, '*': 28, '/': 28,
            '<': 28, '>': 28, '=': 28, ':': 17, ';': 17, ',': 17, "'": 56, '.': 56,
            '(': 17, ')': 17, '[': 17, ']': 17, '{': 17, '}': 17, 'WhiteSpace': 17,
            '\n': 17, 'Symbols': 49},

        6: {'Letter': 21, 'Digit': 21, '_': 21, '+': 21, '-': 21, '*': 13, '/': 21,
            '<': 21, '>': 21, '=': 21, ':': 21, ';': 21, ',': 21, "'": 21, '.': 21,
            '(': 21, ')': 21, '[': 21, ']': 21, '{': 21, '}': 21, 'WhiteSpace': 21,
            '\n': 50, 'Symbols': 50},

        7: {'Letter': 7, 'Digit': 7, '_': 7, '+': 7, '-': 7, '*': 7, '/': 7,
            '<': 7, '>': 7, '=': 7, ':': 7, ';': 7, ',': 7, "'": 7, '.': 7,
            '(': 7, ')': 7, '[': 7, ']': 7, '{': 51, '}': 22, 'WhiteSpace': 7,
            '\n': 52, 'Symbols': 46},

        8: {'Letter': 53, 'Digit': 53, '_': 53, '+': 53, '-': 53, '*': 53, '/': 53,
            '<': 23, '>': 24, '=': 25, ':': 25, ';': 25, ',': 25, "'": 53, '.': 53,
            '(': 25, ')': 25, '[': 25, ']': 25, '{': 25, '}': 25, 'WhiteSpace': 25,
            '\n': 53, 'Symbols': 53},

        9: {'Letter': 54, 'Digit': 54, '_': 54, '+': 54, '-': 54, '*': 54, '/': 54,
            '<': 30, '>': 29, '=': 30, ':': 30, ';': 30, ',': 30, "'": 54, '.': 54,
            '(': 30, ')': 30, '[': 30, ']': 30, '{': 30, '}': 30, 'WhiteSpace': 30,
            '\n': 54, 'Symbols': 54},

        10: {'Letter': 55, 'Digit': 55, '_': 55, '+': 55, '-': 55, '*': 55, '/': 55,
            '<': 32, '>': 31, '=': 32, ':': 32, ';': 32, ',': 32, "'": 55, '.': 55,
            '(': 32, ')': 32, '[': 32, ']': 32, '{': 32, '}': 32, 'WhiteSpace': 32,
            '\n': 55, 'Symbols': 55},

        11: {'Letter': 11, 'Digit': 11, '_': 11, '+': 11, '-': 11, '*': 11, '/': 11,
            '<': 11, '>': 11, '=': 11, ':': 11, ';': 11, ',': 11, "'": 11, '.': 33,
            '(': 11, ')': 11, '[': 11, ']': 11, '{': 11, '}': 11, 'WhiteSpace': 11,
            '\n': 56, 'Symbols': 11}
    }


    # Errores
    Error = {
        
        "44 Error": 44,
        "45 Error": 45,
        "46 Error": 46,
        "47 Error": 47,
        "48 Error": 48,
        "49 Error": 49,
        "50 Error": 50,
        "51 Error": 51,
        "52 Error": 52,
        "53 Error": 53,
        "54 Error": 54,
        "55 Error": 55,
        "56 Error": 56,
        "57 Error": 57,
    }

    # CHECA LA UBICACION DE LA TABLA DE TRANSICIONES Y REGRESA LA UBICACION O ERROR

    if ubicacion in transition_table:
        #CHECA SI ES UNA LETRA 
        if char.isalpha():
            if "Letter" in transition_table[ubicacion]:
                if transition_table[ubicacion]["Letter"] in Error:
                    numberError = transition_table[ubicacion]["Letter"]
                    print(Error[numberError])
                    sys.exit()
                return transition_table[ubicacion]["Letter"]
        # CHECA SI ES UN DIGITO
        if char.isdigit():
            if "Digit" in transition_table[ubicacion]:
                if transition_table[ubicacion]["Digit"] in Error:
                    numberError = transition_table[ubicacion]["Digit"]
                    print(Error[numberError])
                    sys.exit()
                else:
                    return transition_table[ubicacion]["Digit"]
        # CHECA SI ES UN ESPACIO
        if char.isspace():
            if "WhiteSpace" in transition_table[ubicacion]:
                if transition_table[ubicacion]["WhiteSpace"] in Error:
                    numberError = transition_table[ubicacion]["WhiteSpace"]
                    print(Error[numberError])
                    sys.exit()
                else:
                    return transition_table[ubicacion]["WhiteSpace"]
        # CHECA SI EL CHAR ESTA EN LA TABLA DE TRANSICIONES
        if char in transition_table[ubicacion]:
            # print("Char", char)
            if transition_table[ubicacion][char] in Error:
                numberError = transition_table[ubicacion][char]
                print(Error[numberError])
                sys.exit()
            return transition_table[ubicacion][char]
        
        # CHECA SI ES UN SYMBOLO
        if not char.isalpha() and not char.isdigit():
            if "Symbols" in transition_table[ubicacion]:
                if transition_table[ubicacion]["Symbols"] in Error:
                    numberError = transition_table[ubicacion]["Symbols"]
                    print(Error[numberError])
                    sys.exit()
                else:
                    return transition_table[ubicacion]["Symbols"]
    else:
        return -1