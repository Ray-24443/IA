# =========================================================
# DEFINICIÓN DEL GRAFO
# =========================================================
# Grafo representado como lista de adyacencia
grafo = {
    'A': ['B', 'C'],  # A conecta con B y C
    'B': ['D', 'E'],  # B conecta con D y E
    'C': ['F'],       # C conecta con F
    'D': [],          # D no tiene vecinos
    'E': ['F'],       # E conecta con F
    'F': []           # F es nodo objetivo
}

# =========================================================
# FUNCIÓN DFS (BÚSQUEDA EN PROFUNDIDAD)
# =========================================================
def dfs(grafo, inicio, objetivo):
    """
    Realiza una búsqueda en profundidad (Depth-First Search).

    Este algoritmo explora un camino completo antes de retroceder,
    utilizando una estructura tipo pila (LIFO).

    Parámetros:
    grafo (dict): Representación del grafo
    inicio (str): Nodo inicial
    objetivo (str): Nodo objetivo

    Retorna:
    list: Camino encontrado desde inicio hasta objetivo
          o None si no existe
    """

    # Pila que almacena caminos
    pila = [[inicio]]

    # Conjunto de nodos visitados
    visitados = set()

    # Bucle principal
    while pila:
        # Se toma el último elemento (LIFO)
        camino = pila.pop()

        # Último nodo del camino
        nodo = camino[-1]

        # Si encontramos el objetivo
        if nodo == objetivo:
            return camino

        # Si no ha sido visitado
        if nodo not in visitados:
            visitados.add(nodo)

            # Se agregan los vecinos a la pila
            for vecino in grafo[nodo]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                pila.append(nuevo_camino)

    # Si no hay solución
    return None


# =========================================================
# EJECUCIÓN DEL PROGRAMA
# =========================================================

# Ejecutamos la búsqueda desde A hasta F
resultado = dfs(grafo, 'A', 'F')

# Mostramos el resultado
print("Resultado de búsqueda en profundidad:", resultado)