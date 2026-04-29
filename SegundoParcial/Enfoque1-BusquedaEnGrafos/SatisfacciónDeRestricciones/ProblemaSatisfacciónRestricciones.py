# ================== PROBLEMA CSP BASE ==================

# Variables del problema (nodos del grafo)
variables = ['A', 'B', 'C', 'D']  # Cada nodo es una variable

# Dominio: valores posibles para cada variable (colores)
dominios = {
    'A': ['Rojo', 'Verde', 'Azul'],  # Colores posibles para A
    'B': ['Rojo', 'Verde', 'Azul'],  # Colores posibles para B
    'C': ['Rojo', 'Verde', 'Azul'],  # Colores posibles para C
    'D': ['Rojo', 'Verde', 'Azul']   # Colores posibles para D
}

# Restricciones: nodos adyacentes no pueden tener el mismo color
vecinos = {
    'A': ['B', 'C'],  # A no puede ser igual que B o C
    'B': ['A', 'C', 'D'],  # B no puede ser igual que A, C o D
    'C': ['A', 'B', 'D'],  # C no puede ser igual que A, B o D
    'D': ['B', 'C']   # D no puede ser igual que B o C
}