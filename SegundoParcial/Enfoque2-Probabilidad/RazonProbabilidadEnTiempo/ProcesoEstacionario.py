# =========================================
# PROCESO ESTACIONARIO (SIMULACIÓN)
# =========================================

import random

# Estados posibles
estados = ["Soleado", "Lluvioso"]

# Probabilidades fijas (no cambian en el tiempo)
probabilidades = {
    "Soleado": 0.7,
    "Lluvioso": 0.3
}

# Función para generar estados
def generar_estado():
    r = random.random()  # Número aleatorio entre 0 y 1

    # Seleccionamos estado basado en probabilidad
    if r < probabilidades["Soleado"]:
        return "Soleado"
    else:
        return "Lluvioso"

# Simulación
print("Simulación de proceso estacionario:")
for t in range(10):  # 10 instantes de tiempo
    estado = generar_estado()
    print(f"Tiempo {t}: {estado}")