# ================== BÚSQUEDA TABÚ ==================

# Definición del grafo
grafo = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'D': 4, 'E': 1},
    'C': {'A': 5, 'F': 3},
    'D': {'B': 4},
    'E': {'B': 1, 'F': 2},
    'F': {'C': 3, 'E': 2}
}

# Definición de la heurística
heuristica = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 0
}

# Función de búsqueda tabú
def tabu_search(inicio, iteraciones=10, tamaño_tabu=3):
    
    actual = inicio  # Nodo actual
    mejor = inicio   # Mejor nodo encontrado
    tabu = []        # Lista tabú (memoria)
    camino = [actual]  # Registro del camino
    
    # Iterar número definido de veces
    for i in range(iteraciones):
        
        vecinos = grafo[actual]  # Obtener vecinos
        
        # Filtrar vecinos que no estén en la lista tabú
        candidatos = [v for v in vecinos if v not in tabu]
        
        # Si no hay candidatos, terminar
        if not candidatos:
            break
        
        # Elegir el vecino con mejor heurística
        siguiente = min(candidatos, key=lambda x: heuristica[x])
        
        # Agregar nodo actual a lista tabú
        tabu.append(actual)
        
        # Limitar tamaño de lista tabú
        if len(tabu) > tamaño_tabu:
            tabu.pop(0)  # Eliminar el más antiguo
        
        actual = siguiente  # Moverse al siguiente nodo
        camino.append(actual)  # Guardar en camino
        
        # Actualizar mejor nodo encontrado
        if heuristica[actual] < heuristica[mejor]:
            mejor = actual
    
    return camino  # Retornar camino

# Ejecutar desde A
resultado = tabu_search('A')

# Imprimir resultado
print("Camino encontrado:", resultado)