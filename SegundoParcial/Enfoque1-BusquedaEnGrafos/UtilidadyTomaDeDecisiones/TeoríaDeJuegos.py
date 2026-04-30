# ================================
# TEORIA DE JUEGOS - EQUILIBRIO DE NASH
# ================================

# Grafo del juego:
# Jugador1 -> Jugador2 -> Resultado
grafo = {
    'Jugador1': ['Jugador2'],  # Jugador1 influye en Jugador2
    'Jugador2': ['Resultado'],
    'Resultado': []
}

# Estrategias de cada jugador
estrategias_j1 = ['Cooperar', 'Traicionar']
estrategias_j2 = ['Cooperar', 'Traicionar']

# Matriz de pagos (Jugador1, Jugador2)
# (pago_j1, pago_j2)
pagos = {
    ('Cooperar', 'Cooperar'): (3, 3),
    ('Cooperar', 'Traicionar'): (0, 5),
    ('Traicionar', 'Cooperar'): (5, 0),
    ('Traicionar', 'Traicionar'): (1, 1)
}

# Función para verificar equilibrio de Nash
def es_equilibrio(j1, j2):
    pago_actual = pagos[(j1, j2)]  # Pago actual

    # Revisamos si Jugador1 mejora cambiando
    for alt_j1 in estrategias_j1:
        if pagos[(alt_j1, j2)][0] > pago_actual[0]:
            return False  # Puede mejorar → no es equilibrio

    # Revisamos si Jugador2 mejora cambiando
    for alt_j2 in estrategias_j2:
        if pagos[(j1, alt_j2)][1] > pago_actual[1]:
            return False  # Puede mejorar → no es equilibrio

    return True  # Nadie mejora → equilibrio

# Buscamos equilibrios
for j1 in estrategias_j1:
    for j2 in estrategias_j2:
        if es_equilibrio(j1, j2):
            print("Equilibrio de Nash:", (j1, j2))