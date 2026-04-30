# ================================
# ACONDICIONAMIENTO DEL CORTE
# ================================

# Grafo con ciclo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C']
}

# Dominio de colores
colores = ['Rojo', 'Verde']

# Variables del corte (rompen el ciclo)
cutset = ['C']  # Eliminando C queda un árbol

# Función para verificar consistencia
def es_valido(variable, valor, asignacion):
    for vecino in grafo[variable]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False
    return True

# Backtracking simple
def backtracking(variables, asignacion):
    if len(asignacion) == len(variables):
        return asignacion

    variable = [v for v in variables if v not in asignacion][0]

    for valor in colores:
        if es_valido(variable, valor, asignacion):
            asignacion[variable] = valor
            resultado = backtracking(variables, asignacion)

            if resultado:
                return resultado

            del asignacion[variable]

    return None

# Probamos todas las combinaciones del cutset
from itertools import product

for valores in product(colores, repeat=len(cutset)):
    asignacion = dict(zip(cutset, valores))

    # Variables restantes (árbol)
    restantes = [v for v in grafo if v not in cutset]

    resultado = backtracking(restantes, asignacion.copy())

    if resultado:
        print("Solución encontrada:", resultado)
        break
else:
    print("No hay solución")