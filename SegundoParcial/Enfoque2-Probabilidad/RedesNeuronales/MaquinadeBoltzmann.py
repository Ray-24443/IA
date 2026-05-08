# ==========================================
# MÁQUINA DE BOLTZMANN
# ==========================================

# Importamos random
import random

# Estado inicial
estado = random.randint(0, 1)

# Iteraciones
for i in range(10):

    # Número aleatorio
    probabilidad = random.random()

    # Cambio de estado
    if probabilidad > 0.5:
        estado = 1
    else:
        estado = 0

    # Resultado
    print(estado)