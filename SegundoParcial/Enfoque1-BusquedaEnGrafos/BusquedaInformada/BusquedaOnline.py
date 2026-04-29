# ================== BÚSQUEDA ONLINE ==================

# Definición del grafo
grafo = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'D': 4, 'E': 1},
    'C': {'A': 5, 'F': 3},
    'D': {'B': 4},
    'E': {'B': 1, 'F': 2},
    'F': {'C': 3, 'E': 2}
}

# Nodo objetivo
objetivo = 'F'  # Nodo meta

# Función de búsqueda online
def busqueda_online(inicio):
    
    actual = inicio  # Nodo actual
    visitados = set()  # Conjunto de nodos visitados
    camino = [actual]  # Registro del camino
    
    # Mientras no se llegue al objetivo
    while actual != objetivo:
        
        visitados.add(actual)  # Marcar como visitado
        
        vecinos = grafo[actual]  # Obtener vecinos
        
        siguiente = None  # Inicializar siguiente nodo
        
        # Buscar un vecino no visitado
        for v in vecinos:
            if v not in visitados:
                siguiente = v
                break
        
        # Si todos están visitados, elegir cualquiera
        if siguiente is None:
            siguiente = list(vecinos.keys())[0]
        
        actual = siguiente  # Moverse al siguiente nodo
        camino.append(actual)  # Guardar en camino
    
    return camino  # Retornar camino encontrado

# Ejecutar desde A
resultado = busqueda_online('A')

# Mostrar resultado
print("Camino encontrado:", resultado)  