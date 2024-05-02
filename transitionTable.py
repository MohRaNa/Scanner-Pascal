import sys

def checkTransitionTable(char, ubicacion):

    transition_table = {

        0: {'Letter': 2, 'Digit': 3, '_': 1, '+': 27, '-': 28, 
            '*': 30, '/': 29, '<': 10, '>': 11, '=': 34, 
            ':': 7, ';': 33, ',': 32, "'": 8, ".": 1,
            "(": 6, ")": 40, "[": 26, "]": 26, "{": 9, "}": 23, 
            "WhiteSpace": 0, "\n": 0, "Symbols": 0},

        1: {'Letter': 2, 'Digit': 44, '_': 44, '+': 44, '-': 44, '*': 44, '/': 44,
            '<': 44, '>': 44, '=': 44, ':': 44, ';': 44, ',': 44, "'": 44, '.': 44,
            "(": 44,")": 44, "[": 44, "]": 44, "{": 44, "}": 44, "WhiteSpace": 44,
            "\n": 44, "Symbols": 44},

        2: {'Letter': 2, 'Digit': 2, '_': 2, '+': 13, '-': 13,
            '*': 13, '/': 13, '<': 13, '>': 13, '=': 13, ':': 12,
            ';': 12, ',': 12, "'": 52, '.': 52,"(": 12, ")": 12, "[": 12,
            "]": 12, "{": 12, "}": 12, "WhiteSpace": 12,
            "\n": 12, "Symbols": 52},

        3: {'Letter': 53, 'Digit': 3, '_': 53, '+': 14, '-': 14, '*': 14, '/': 14,
            '<': 14, '>': 14, '=': 14, ':': 15, ';': 15, ',': 15, "'": 40, '.': 4, 
            "(": 15, ")": 15, "[": 15, "]": 15, "{": 15, "}": 15,
            "WhiteSpace": 15, "\n": 15, "Symbols": 54},

        4: {'Letter': 55, 'Digit': 5, '_': 55, '+': 55, '-': 55, '*': 55,
            '/': 55, '<': 55, '>': 55, '=': 55, ':': 55, ';': 55, ',': 55,
            "'": 55, '.': 55, "(": 55, ")": 55, "[": 55, "]": 55, "{": 55, "}": 55,
            "WhiteSpace": 55, "\n": 55, "Symbols": 55},

        5: {'Letter': 56, 'Digit': 5, '_': 56, '+': 42, '-': 42, '*': 42,
            '/': 42, '<': 42, '>': 42, '=': 42, ':': 42, ';': 42, ',': 42,
            "'": 42, '.': 56, "(": 41, ")": 41, "[": 41, "]": 41, "{": 41, "}": 41,
            "WhiteSpace": 41, "\n": 41, "Symbols": 56},

        6: {'Letter': 45, 'Digit': 45, '_': 45, '+': 45, '-': 45, '*': 16,
            '/': 45, '<': 45, '>': 45, '=': 45, ':': 19, ';': 19, ',': 19,
            "'": 45, '.': 45 , "(": 19, ")": 19, "[": 19, "]": 19, "{": 19, "}": 19,
            "WhiteSpace": 19, "\n": 19, "Symbols": 45},

        7: {'Letter': 46, 'Digit': 46, '_': 46, '+': 46, '-': 46, '*': 46,
            '/': 46, '<': 46, '>': 46, '=': 20, ':': 21, ';': 21, ',': 21, 
            "'": 46, '.': 46, "(": 21, ")": 21, "[": 21, "]": 21, "{": 21, "}": 21,
            "WhiteSpace": 21, "\n": 21, "Symbols": 46},

        8: {'Letter': 8, 'Digit': 8, '_': 8, '+': 8, '-': 8, '*': 8, '/': 8,
            '<': 8, '>': 8, '=': 8, ':': 8, ';': 8, ',': 22, "'": 8, '.': 8,
            "(": 8, ")": 8, "[": 8, "]": 8, "{": 47, "}": 8,
            "WhiteSpace": 8, "\n": 47, "Symbols": 8},

        9: {'Letter': 9, 'Digit': 9, '_': 9, '+': 9, '-': 9, '*': 9, '/': 9, 
            '<': 9, '>': 9, '=': 9, ':': 9, ';': 9, ',': 9, "'": 9, '.': 8,
            "(": 9, ")": 9, "[": 9, "]": 9, "{": 48, "}": 24,
            "WhiteSpace": 9, "\n": 49, "Symbols": 9},

        10: {'Letter': 50, 'Digit': 50, '_': 50, '+': 50, '-': 50, '*': 50,
            '/': 50, '<': 50, '>': 35, '=': 36, ':': 37, ';': 37, ',': 37,
            "'": 50, ".": 50, "(": 37, ")": 37, "[": 37, "]": 37, "{": 37, "}": 37,
            "WhiteSpace": 37, "\n": 50, "Symbols": 50},

        11: {'Letter': 51, 'Digit': 51, '_': 51, '+': 51, '-': 51, '*': 51,
            '/': 51, '<': 51, '>': 51, '=': 38, ':': 39, ';': 39, ',': 39,
            "'": 51, '.': 51, "(": 39, ")": 39, "[": 39, "]": 39, "{": 39, "}": 39,
            "WhiteSpace": 39, "\n": 51, "Symbols": 51},
    }
   # 1 No reconoce al final;
   # 2 Separar Integer y Reales 
   # 3 STRINGS
   # 4 PALABRAS RESERVADAS NO RECONOCIDAS
   # 5 DFA ACTUALIZADO
   # 6 NO RECONOCER LOS TOKENS DE LOS 
   # 7 HACER PRUEBAS

    Error = {
        "43 Error Salto de Linea": 43,
        "44 Error no Continua con Letra": 44,
        "45 Error": 45,
        "46 Error": 46,
        "47 Error Salto de Linea": 47,
        "48 Error {} en Comentarios": 48,
        "49 Error Salto de Linea": 49,
        "50 Error": 50,
        "51 Error": 51,
        "52 Error": 52,
        "53 Error": 53,
        "54 Error Salto de Linea": 54,
        "55 Error No Sigue Digito": 55,
        "56 Error No Sigue Digito": 56
    }

    if ubicacion in transition_table:
        # print("Char: ", char)
        if char.isalpha():
            if "Letter" in transition_table[ubicacion]:
                if transition_table[ubicacion]["Letter"] in Error:
                    numberError = transition_table[ubicacion]["Letter"]
                    print(Error[numberError])
                    sys.exit()
                return transition_table[ubicacion]["Letter"]
        if char.isdigit():
            if "Digit" in transition_table[ubicacion]:
                if transition_table[ubicacion]["Digit"] in Error:
                    numberError = transition_table[ubicacion]["Digit"]
                    print(Error[numberError])
                    sys.exit()
                else:
                    return transition_table[ubicacion]["Digit"]
        if char.isspace():
            if "WhiteSpace" in transition_table[ubicacion]:
                if transition_table[ubicacion]["WhiteSpace"] in Error:
                    numberError = transition_table[ubicacion]["WhiteSpace"]
                    print(Error[numberError])
                    sys.exit()
                else:
                    return transition_table[ubicacion]["WhiteSpace"]
        if char in transition_table[ubicacion]:
            print("Char", char)
            if transition_table[ubicacion][char] in Error:
                numberError = transition_table[ubicacion][char]
                print(Error[numberError])
                sys.exit()
            print(transition_table[ubicacion][char])
            return transition_table[ubicacion][char]
        

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