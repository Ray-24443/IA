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
# FUNCIÓN DLS (NECESARIA PARA IDS)
# =========================================================
def dls(grafo, nodo, objetivo, limite, camino=None):
    if camino is None:
        camino = [nodo]

    if nodo == objetivo:
        return camino

    if limite == 0:
        return None

    for vecino in grafo[nodo]:
        if vecino not in camino:
            resultado = dls(grafo, vecino, objetivo, limite - 1, camino + [vecino])
            if resultado:
                return resultado

    return None

# =========================================================
# FUNCIÓN IDS
# =========================================================
def ids(grafo, inicio, objetivo, max_profundidad):
    """
    Búsqueda en Profundidad Iterativa
    """

    for limite in range(max_profundidad + 1):
        resultado = dls(grafo, inicio, objetivo, limite)
        if resultado:
            return resultado

    return None

# =========================================================
# EJECUCIÓN
# =========================================================
resultado = ids(grafo, 'A', 'F', 5)
print("IDS:", resultado)