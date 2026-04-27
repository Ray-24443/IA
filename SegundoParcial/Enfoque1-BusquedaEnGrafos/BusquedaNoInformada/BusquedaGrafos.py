from collections import deque

# =========================================================
# GRAFO
# =========================================================
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# =========================================================
# FUNCIÓN BÚSQUEDA EN GRAFOS
# =========================================================
def busqueda_grafos(grafo, inicio, objetivo):
    """
    Búsqueda en Grafos (versión general tipo BFS)

    A diferencia de búsqueda en árboles:
    - Aquí se evitan ciclos usando un conjunto de visitados

    Retorna:
    list: Camino encontrado o None
    """

    # Cola para explorar nodos
    cola = deque([[inicio]])

    # Conjunto de nodos visitados
    visitados = set()

    # Bucle principal
    while cola:
        camino = cola.popleft()
        nodo = camino[-1]

        # Si se encuentra el objetivo
        if nodo == objetivo:
            return camino

        # Si no ha sido visitado
        if nodo not in visitados:
            visitados.add(nodo)

            # Se agregan vecinos
            for vecino in grafo[nodo]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    return None


# =========================================================
# EJECUCIÓN
# =========================================================
resultado = busqueda_grafos(grafo, 'A', 'F')
print("Resultado Búsqueda en Grafos:", resultado)