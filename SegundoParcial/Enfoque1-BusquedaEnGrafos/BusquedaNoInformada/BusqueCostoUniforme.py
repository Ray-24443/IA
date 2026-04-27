import heapq  # Se usa para manejar la cola de prioridad

# =========================================================
# DEFINICIÓN DEL GRAFO CON COSTOS
# =========================================================
# Cada nodo tiene una lista de tuplas (vecino, costo)
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# =========================================================
# FUNCIÓN DE BÚSQUEDA DE COSTO UNIFORME (UCS)
# =========================================================
def costo_uniforme(grafo, inicio, objetivo):
    """
    Realiza una búsqueda de costo uniforme.

    Este algoritmo encuentra el camino de menor costo desde un nodo
    inicial hasta un nodo objetivo en un grafo ponderado.

    Parámetros:
    grafo (dict): Diccionario del tipo {nodo: [(vecino, costo)]}
    inicio (str): Nodo inicial
    objetivo (str): Nodo objetivo

    Retorna:
    tuple: (costo_total, camino)
           costo_total -> suma de los costos del camino
           camino -> lista de nodos desde inicio hasta objetivo
           Retorna None si no existe solución
    """

    # Cola de prioridad: (costo acumulado, nodo actual, camino recorrido)
    cola = [(0, inicio, [])]

    # Conjunto para evitar repetir nodos
    visitados = set()

    # Bucle principal
    while cola:
        # Extrae el nodo con menor costo acumulado
        costo, nodo, camino = heapq.heappop(cola)

        # Si ya fue visitado, se ignora
        if nodo in visitados:
            continue

        # Se agrega el nodo al camino
        camino = camino + [nodo]

        # Se marca como visitado
        visitados.add(nodo)

        # Si llegamos al objetivo, retornamos resultado
        if nodo == objetivo:
            return costo, camino

        # Se exploran los vecinos
        for vecino, peso in grafo[nodo]:
            # Se agrega a la cola con el nuevo costo acumulado
            heapq.heappush(cola, (costo + peso, vecino, camino))

    # Si no hay solución
    return None


# =========================================================
# EJECUCIÓN DEL PROGRAMA
# =========================================================

# Se ejecuta la búsqueda desde A hasta F
resultado = costo_uniforme(grafo, 'A', 'F')

# Se imprime el resultado
print("Resultado de costo uniforme:", resultado)