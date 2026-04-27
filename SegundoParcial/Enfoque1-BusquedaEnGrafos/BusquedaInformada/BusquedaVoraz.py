import heapq  # Permite manejar una cola de prioridad

# =========================================================
# GRAFO
# =========================================================
# Representa conexiones entre nodos (sin costos)
grafo = {
    'A': ['B', 'C'],   # A conecta con B y C
    'B': ['D', 'E'],   # B conecta con D y E
    'C': ['F'],        # C conecta con F
    'D': [],           # Nodo hoja
    'E': ['F'],
    'F': []            # Nodo objetivo
}

# =========================================================
# HEURÍSTICA
# =========================================================
# Estimación de distancia al objetivo
heuristica = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 0  # El objetivo siempre tiene heurística 0
}

# =========================================================
# FUNCIÓN BÚSQUEDA VORAZ
# =========================================================
def busqueda_voraz(grafo, inicio, objetivo):
    """
    Búsqueda Voraz (Greedy Best-First Search)

    Este algoritmo selecciona siempre el nodo con menor valor heurístico h(n),
    sin considerar el costo del camino recorrido.

    Parámetros:
    grafo (dict): estructura del grafo
    inicio (str): nodo inicial
    objetivo (str): nodo objetivo

    Retorna:
    list: camino encontrado o None
    """

    # Cola de prioridad: (heurística, nodo, camino)
    cola = [(heuristica[inicio], inicio, [inicio])]

    # Conjunto de nodos visitados
    visitados = set()

    # Bucle principal
    while cola:
        # Extrae el nodo con menor heurística
        h, nodo, camino = heapq.heappop(cola)

        # Si se encuentra el objetivo
        if nodo == objetivo:
            return camino

        # Si no ha sido visitado
        if nodo not in visitados:
            visitados.add(nodo)

            # Se agregan los vecinos a la cola
            for vecino in grafo[nodo]:
                heapq.heappush(
                    cola,
                    (heuristica[vecino], vecino, camino + [vecino])
                )

    return None


# =========================================================
# EJECUCIÓN
# =========================================================
resultado = busqueda_voraz(grafo, 'A', 'F')
print("Resultado Búsqueda Voraz:", resultado)