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
# FUNCIÓN BIDIRECCIONAL
# =========================================================
def bidireccional(grafo, inicio, objetivo):
    """
    Búsqueda Bidireccional

    Este algoritmo busca simultáneamente desde:
    - Nodo inicial
    - Nodo objetivo

    Cuando ambas búsquedas se encuentran, se construye el camino.

    Retorna:
    list: Camino encontrado
    """

    # Caso trivial
    if inicio == objetivo:
        return [inicio]

    # Diccionarios que guardan caminos
    frente = {inicio: [inicio]}
    atras = {objetivo: [objetivo]}

    # Bucle principal
    while frente and atras:
        nuevo_frente = {}

        # Expansión desde el inicio
        for nodo in frente:
            for vecino in grafo[nodo]:

                # Si el nodo se encuentra con la búsqueda inversa
                if vecino in atras:
                    return frente[nodo] + atras[vecino][::-1]

                # Si no ha sido visitado
                if vecino not in frente:
                    nuevo_frente[vecino] = frente[nodo] + [vecino]

        frente = nuevo_frente

    return None


# =========================================================
# EJECUCIÓN
# =========================================================
resultado = bidireccional(grafo, 'A', 'F')
print("Resultado Bidireccional:", resultado)