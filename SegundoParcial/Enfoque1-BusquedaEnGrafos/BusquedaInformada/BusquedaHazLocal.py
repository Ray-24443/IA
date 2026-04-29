# ================== BÚSQUEDA DE HAZ LOCAL ==================

# Definición del grafo
grafo = {
    'A': {'B': 2, 'C': 5},  # Nodo A conectado a B y C
    'B': {'A': 2, 'D': 4, 'E': 1},  # Nodo B conectado a A, D y E
    'C': {'A': 5, 'F': 3},  # Nodo C conectado a A y F
    'D': {'B': 4},  # Nodo D conectado a B
    'E': {'B': 1, 'F': 2},  # Nodo E conectado a B y F
    'F': {'C': 3, 'E': 2}  # Nodo F conectado a C y E
}

# Definición de heurística (menor es mejor)
heuristica = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 0
}

# Función de búsqueda de haz local
def beam_search(inicio, k=2, iteraciones=5):
    
    estados = [inicio]  # Lista de estados actuales (inicia con el nodo inicial)
    
    # Iterar cierto número de veces
    for i in range(iteraciones):
        
        todos_vecinos = []  # Lista para guardar todos los vecinos
        
        # Recorrer cada estado actual
        for estado in estados:
            
            vecinos = grafo[estado].keys()  # Obtener vecinos del estado
            
            # Agregar vecinos a la lista general
            for v in vecinos:
                todos_vecinos.append(v)
        
        # Ordenar vecinos por heurística (menor es mejor)
        ordenados = sorted(todos_vecinos, key=lambda x: heuristica[x])
        
        # Seleccionar los k mejores estados
        estados = ordenados[:k]
    
    return estados  # Retornar mejores estados encontrados

# Ejecutar algoritmo
resultado = beam_search('A')

# Imprimir resultado
print("Estados finales:", resultado)