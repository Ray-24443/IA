# ==========================================
# RED NEURONAL SIMPLE
# ==========================================

# Importamos random
import random

# ------------------------------------------
# Función sigmoide
# ------------------------------------------
def sigmoide(x):

    # Fórmula sigmoide
    return 1 / (1 + 2.71828 ** (-x))

# ------------------------------------------
# Datos de entrada
# ------------------------------------------
entradas = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# ------------------------------------------
# Salidas esperadas
# ------------------------------------------
salidas = [0, 1, 1, 1]

# ------------------------------------------
# Pesos iniciales aleatorios
# ------------------------------------------
w1 = random.random()
w2 = random.random()

# ------------------------------------------
# Bias
# ------------------------------------------
b = random.random()

# ------------------------------------------
# Learning rate
# ------------------------------------------
lr = 0.5

# ------------------------------------------
# Entrenamiento
# ------------------------------------------
for epoca in range(1000):

    # Recorremos datos
    for i in range(len(entradas)):

        # Valores de entrada
        x1 = entradas[i][0]
        x2 = entradas[i][1]

        # Salida esperada
        y = salidas[i]

        # Suma ponderada
        suma = (x1 * w1) + (x2 * w2) + b

        # Predicción
        prediccion = sigmoide(suma)

        # Error
        error = y - prediccion

        # Ajustamos peso 1
        w1 = w1 + (lr * error * x1)

        # Ajustamos peso 2
        w2 = w2 + (lr * error * x2)

        # Ajustamos bias
        b = b + (lr * error)

# ------------------------------------------
# Resultados finales
# ------------------------------------------
print("Resultados finales")

# Recorremos entradas
for entrada in entradas:

    # Calculamos suma
    suma = (entrada[0] * w1) + (entrada[1] * w2) + b

    # Calculamos salida
    salida = sigmoide(suma)

    # Mostramos resultado
    print(entrada, salida)