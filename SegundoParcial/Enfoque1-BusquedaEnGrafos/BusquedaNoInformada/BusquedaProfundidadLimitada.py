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
# FUNCIÓN DLS
# =========================================================
def dls(grafo, nodo, objetivo, limite, camino=None):
    """
    Búsqueda en Profundidad Limitada (Depth Limited Search)

    Parámetros:
    grafo (dict): Grafo
    nodo (str): Nodo actual
    objetivo (str): Nodo objetivo
    limite (int): Profundidad máxima permitida
    camino (list): Camino recorrido

    Retorna:
    list: Camino encontrado o None
    """

    # Inicializa el camino
    if camino is None:
        camino = [nodo]

    # Si se encuentra el objetivo
    if nodo == objetivo:
        return camino

    # Si se alcanza el límite
    if limite == 0:
        return None

    # Explorar vecinos
    for vecino in grafo[nodo]:
        if vecino not in camino:
            resultado = dls(grafo, vecino, objetivo, limite - 1, camino + [vecino])
            if resultado:
                return resultado

    return None


# =========================================================
# EJECUCIÓN
# =========================================================
print("DLS:", dls(grafo, 'A', 'F', 2))