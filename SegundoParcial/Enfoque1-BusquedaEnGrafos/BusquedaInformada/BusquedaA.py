import heapq

# =========================================================
# GRAFO CON COSTOS
# =========================================================
# Cada conexión tiene un costo (peso)
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# =========================================================
# HEURÍSTICA
# =========================================================
heuristica = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 0
}

# =========================================================
# FUNCIÓN A*
# =========================================================
def a_estrella(grafo, inicio, objetivo):
    """
    Búsqueda A* (A Star)

    Combina:
    g(n) = costo real desde el inicio
    h(n) = estimación al objetivo

    Fórmula:
    f(n) = g(n) + h(n)

    Retorna:
    tuple: (costo_total, camino)
    """

    # Cola de prioridad: (f, costo, nodo, camino)
    cola = [(heuristica[inicio], 0, inicio, [inicio])]

    visitados = set()

    while cola:
        f, costo, nodo, camino = heapq.heappop(cola)

        if nodo == objetivo:
            return costo, camino

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino, peso in grafo[nodo]:
                nuevo_costo = costo + peso
                nuevo_f = nuevo_costo + heuristica[vecino]

                heapq.heappush(
                    cola,
                    (nuevo_f, nuevo_costo, vecino, camino + [vecino])
                )

    return None


# =========================================================
# EJECUCIÓN
# =========================================================
resultado = a_estrella(grafo, 'A', 'F')
print("Resultado A*:", resultado)