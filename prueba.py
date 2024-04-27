def checkTransitionTable(char, ubicacion):
    transition_table = {
        0: {'Letter': 2, 'Digit': 3, '_': 1, '+': 27, '-': 28, 
            '*': 30, '/': 29, '<': 10, '>': 11, '=': 34, 
            ':': 7, ';': 33, ',': 32, "'": 8, 
            "(": 31, ")": 6, "[": 40, "]": 26, "{": 26, "}": 23, 
            "White Space": 9, "\n": 0, "Otros Simbolos": 0},
        # El resto de la tabla de transición aquí
    }

    # Verificar si la ubicación está en la tabla de transición
    if ubicacion in transition_table:
        # Verificar si el carácter está en la lista de transición para esa ubicación
        if char in transition_table[ubicacion]:
            # Obtener el número asociado al tipo de transición
            numero_transicion = transition_table[ubicacion][char]
            # Devolver el número de la transición
            return numero_transicion
        else:
            return None  # Carácter no encontrado en la ubicación dada
    else:
        return None  # Ubicación no encontrada en la tabla de transición

# Ejemplo de uso
ubicacion_actual = 0
caracter_a_buscar = "Letter"
numero_transicion = checkTransitionTable(caracter_a_buscar, ubicacion_actual)
print("Número de la transición:", numero_transicion)
