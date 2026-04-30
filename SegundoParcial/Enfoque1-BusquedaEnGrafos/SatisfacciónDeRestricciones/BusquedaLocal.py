# ================================
# MINIMOS CONFLICTOS
# ================================

import random  # Para generar valores aleatorios

# Grafo (mismo ejemplo)
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Dominio de colores
colores = ['Rojo', 'Verde', 'Azul']

# Generamos una asignación inicial aleatoria
asignacion = {var: random.choice(colores) for var in grafo}

# Función que cuenta conflictos de una variable
def contar_conflictos(variable, valor):
    conflictos = 0
    for vecino in grafo[variable]:
        if asignacion[vecino] == valor:
            conflictos += 1  # Incrementamos si hay conflicto
    return conflictos

# Algoritmo de mínimos conflictos
def minimos_conflictos(max_iter=1000):
    for i in range(max_iter):

        # Revisamos si ya no hay conflictos
        conflictos_totales = []
        for var in grafo:
            if contar_conflictos(var, asignacion[var]) > 0:
                conflictos_totales.append(var)

        if not conflictos_totales:
            return asignacion  # Solución encontrada

        # Elegimos variable con conflicto
        variable = random.choice(conflictos_totales)

        # Elegimos el mejor valor (menos conflictos)
        mejor_valor = None
        min_conflictos = float('inf')

        for valor in colores:
            c = contar_conflictos(variable, valor)
            if c < min_conflictos:
                min_conflictos = c
                mejor_valor = valor

        # Asignamos el mejor valor
        asignacion[variable] = mejor_valor

    return None  # No encontró solución

# Ejecutamos
resultado = minimos_conflictos()

if resultado:
    print("Solución encontrada:", resultado)
else:
    print("No se encontró solución")