# =========================================================
# GRAFO
# =========================================================
# Grafo simple (sin costos)
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# =========================================================
# FUNCIÓN HEURÍSTICA
# =========================================================
def heuristica(nodo):
    """
    Función heurística h(n)

    Esta función estima la distancia desde un nodo hasta el objetivo.

    Mientras menor sea el valor, más cerca está del objetivo.

    Parámetros:
    nodo (str): nodo actual

    Retorna:
    int: valor heurístico
    """

    valores = {
        'A': 5,
        'B': 3,
        'C': 2,
        'D': 6,
        'E': 1,
        'F': 0  # Nodo objetivo
    }

    return valores[nodo]

# =========================================================
# EJEMPLO DE USO DE LA HEURÍSTICA
# =========================================================
print("Valor heurístico de A:", heuristica('A'))
print("Valor heurístico de C:", heuristica('C'))
print("Valor heurístico de F:", heuristica('F'))