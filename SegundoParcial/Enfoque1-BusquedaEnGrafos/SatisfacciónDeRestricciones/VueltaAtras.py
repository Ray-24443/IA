# ================== BACKTRACKING ==================

# Definir variables (nodos del grafo)
variables = ['A', 'B', 'C', 'D']  # Lista de nodos a colorear

# Definir dominios (colores posibles)
dominios = {
    'A': ['Rojo', 'Verde', 'Azul'],  # Colores posibles para A
    'B': ['Rojo', 'Verde', 'Azul'],  # Colores posibles para B
    'C': ['Rojo', 'Verde', 'Azul'],  # Colores posibles para C
    'D': ['Rojo', 'Verde', 'Azul']   # Colores posibles para D
}

# Definir restricciones (vecinos no pueden tener mismo color)
vecinos = {
    'A': ['B', 'C'],  # A conectado con B y C
    'B': ['A', 'C', 'D'],  # B conectado con A, C y D
    'C': ['A', 'B', 'D'],  # C conectado con A, B y D
    'D': ['B', 'C']  # D conectado con B y C
}

# Función que verifica si asignar un valor es válido
def es_valido(variable, valor, asignacion):
    
    # Recorrer vecinos de la variable
    for vecino in vecinos[variable]:
        
        # Si el vecino ya tiene valor asignado
        if vecino in asignacion:
            
            # Si el valor es igual, hay conflicto
            if asignacion[vecino] == valor:
                return False  # No válido
    
    return True  # Válido si no hay conflictos

# Función principal de backtracking
def backtracking(asignacion={}):
    
    # Si todas las variables están asignadas
    if len(asignacion) == len(variables):
        return asignacion  # Retornar solución
    
    # Buscar variable no asignada
    for variable in variables:
        if variable not in asignacion:
            break  # Seleccionar la primera libre
    
    # Probar cada valor del dominio
    for valor in dominios[variable]:
        
        # Verificar si el valor es válido
        if es_valido(variable, valor, asignacion):
            
            asignacion[variable] = valor  # Asignar valor
            
            resultado = backtracking(asignacion)  # Llamada recursiva
            
            if resultado:
                return resultado  # Si encuentra solución
            
            del asignacion[variable]  # Deshacer asignación
    
    return None  # No hay solución

# Ejecutar algoritmo
print("Backtracking:", backtracking())