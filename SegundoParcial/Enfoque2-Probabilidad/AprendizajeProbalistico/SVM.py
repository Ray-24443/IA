# ==========================================
# SVM SIMPLE
# ==========================================

# Datos
# x1, x2, clase
datos = [
    [1, 1, -1],
    [2, 2, -1],
    [4, 4, 1],
    [5, 5, 1]
]

# Pesos
w1 = 0
w2 = 0

# Bias
b = 0

# Learning rate
lr = 0.1

# Entrenamiento
for epoca in range(10):

    # Recorremos datos
    for dato in datos:

        # Valores
        x1 = dato[0]
        x2 = dato[1]
        y = dato[2]

        # Resultado
        resultado = w1 * x1 + w2 * x2 + b

        # Verificamos clasificación
        if y * resultado <= 0:

            # Ajustamos pesos
            w1 = w1 + lr * y * x1
            w2 = w2 + lr * y * x2

            # Ajustamos bias
            b = b + lr * y

# Resultado final
print("Pesos finales")
print(w1, w2, b)