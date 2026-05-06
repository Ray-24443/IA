# =========================================
# PROCESO DE MARKOV (CADENA)
# =========================================

import random

# Estados posibles
estados = ["Soleado", "Lluvioso"]

# Matriz de transición
# P(siguiente_estado | estado_actual)
transiciones = {
    "Soleado": {"Soleado": 0.8, "Lluvioso": 0.2},
    "Lluvioso": {"Soleado": 0.4, "Lluvioso": 0.6}
}

# Función para obtener siguiente estado
def siguiente_estado(actual):
    r = random.random()  # Número aleatorio

    acumulado = 0

    # Recorremos probabilidades
    for estado, prob in transiciones[actual].items():
        acumulado += prob

        if r < acumulado:
            return estado


# Simulación
estado_actual = "Soleado"

print("Simulación de proceso de Markov:")
for t in range(10):
    print(f"Tiempo {t}: {estado_actual}")
    estado_actual = siguiente_estado(estado_actual)