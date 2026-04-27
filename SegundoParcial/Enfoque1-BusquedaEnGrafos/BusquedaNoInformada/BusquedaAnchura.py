from collections import deque  # Importamos deque para usar una cola eficiente


grafo = {
    'A': ['B', 'C'],  # A se conecta con B y C
    'B': ['D', 'E'],  # B se conecta con D y E
    'C': ['F'],       # C se conecta con F
    'D': [],          # D no tiene vecinos
    'E': ['F'],       # E se conecta con F
    'F': []           # F es nodo final
}

# FUNCIÓN BFS

def bfs(grafo, inicio, objetivo):
    """
    Realiza una búsqueda en anchura (Breadth-First Search).

    Parámetros:
    grafo (dict): Diccionario que representa el grafo.
    inicio (str): Nodo desde donde comienza la búsqueda.
    objetivo (str): Nodo que se desea encontrar.

    Retorna:
    list: Lista con el camino desde inicio hasta objetivo.
          Retorna None si no existe un camino.
    """

    # Cola que almacenará los caminos a explorar
    # Cada elemento es una lista que representa un camino
    cola = deque([[inicio]])

    # Conjunto para registrar los nodos ya visitados
    visitados = set()

    # Bucle principal: se ejecuta mientras haya caminos por explorar
    while cola:
        # Extrae el primer camino de la cola (FIFO)
        camino = cola.popleft()

        # Obtiene el último nodo del camino actual
        nodo = camino[-1]

        # Verifica si el nodo actual es el objetivo
        if nodo == objetivo:
            return camino  # Retorna el camino encontrado

        # Si el nodo no ha sido visitado
        if nodo not in visitados:
            # Se marca como visitado para no repetirlo
            visitados.add(nodo)

            # Recorre todos los vecinos del nodo actual
            for vecino in grafo[nodo]:
                # Crea un nuevo camino agregando el vecino
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)

                # Agrega el nuevo camino a la cola
                cola.append(nuevo_camino)

    # Si se vacía la cola y no se encontró el objetivo
    return None

# EJECUCIÓN DEL PROGRAMA
 

# Se llama a la función BFS indicando:
# - Nodo inicial: 'A'
# - Nodo objetivo: 'F'
resultado = bfs(grafo, 'A', 'F')

# Se imprime el resultado en pantalla
print("Resultado de la búsqueda en anchura:", resultado)