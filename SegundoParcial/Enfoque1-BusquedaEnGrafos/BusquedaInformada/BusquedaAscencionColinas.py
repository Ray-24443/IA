# ================== HILL CLIMBING ==================

# Definición del grafo como diccionario de adyacencia con costos
grafo = {
    'A': {'B': 2, 'C': 5},   # Nodo A conectado con B y C
    'B': {'A': 2, 'D': 4, 'E': 1},  # Nodo B conectado con A, D y E
    'C': {'A': 5, 'F': 3},   # Nodo C conectado con A y F
    'D': {'B': 4},           # Nodo D conectado con B
    'E': {'B': 1, 'F': 2},   # Nodo E conectado con B y F
    'F': {'C': 3, 'E': 2}    # Nodo F conectado con C y E
}

# Definición de la heurística (valor estimado al objetivo)
heuristica = {
    'A': 7,  # Valor heurístico del nodo A
    'B': 6,  # Valor heurístico del nodo B
    'C': 4,  # Valor heurístico del nodo C
    'D': 3,  # Valor heurístico del nodo D
    'E': 2,  # Valor heurístico del nodo E
    'F': 0   # Nodo objetivo (mejor valor)
}

# Definición de la función principal del algoritmo
def hill_climbing(inicio):
    
    actual = inicio  # Nodo actual inicia en el nodo de entrada
    camino = [actual]  # Lista que guarda el camino recorrido
    
    while True:  # Ciclo infinito hasta encontrar solución
        
        vecinos = grafo[actual]  # Obtener vecinos del nodo actual
        
        mejor_vecino = None  # Variable para guardar el mejor vecino
        mejor_valor = heuristica[actual]  # Valor heurístico actual
        
        # Recorrer todos los vecinos del nodo actual
        for vecino in vecinos:
            
            # Comparar si el vecino tiene mejor heurística (menor valor)
            if heuristica[vecino] < mejor_valor:
                
                mejor_vecino = vecino  # Guardar mejor vecino
                mejor_valor = heuristica[vecino]  # Actualizar valor
        
        # Si no se encontró un mejor vecino, se detiene
        if mejor_vecino is None:
            break
        
        actual = mejor_vecino  # Moverse al mejor vecino
        camino.append(actual)  # Agregar al camino
    
    return camino  # Retornar el camino encontrado

# Ejecutar el algoritmo desde el nodo A
resultado = hill_climbing('A')

# Imprimir el resultado final
print("Camino encontrado:", resultado)