# ==========================================
# ADALINE
# ==========================================

# Datos
entradas = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Salidas
salidas = [0, 1, 1, 1]

# Pesos
w1 = 0.1
w2 = 0.1
b = 0.1

# Learning rate
lr = 0.1

# Entrenamiento
for epoca in range(20):

    # Recorremos entradas
    for i in range(len(entradas)):

        # Valores
        x1 = entradas[i][0]
        x2 = entradas[i][1]
        y = salidas[i]

        # Salida lineal
        salida = (x1 * w1) + (x2 * w2) + b
print(w1, w2, b)