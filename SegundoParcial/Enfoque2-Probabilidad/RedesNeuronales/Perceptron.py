# ==========================================
# PERCEPTRÓN
# ==========================================

# Entradas
entradas = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Salidas esperadas OR
salidas = [0, 1, 1, 1]

# Pesos
w1 = 0
w2 = 0

# Bias
b = 0

# Tasa de aprendizaje
lr = 0.1

# Entrenamiento
for epoca in range(10):

    # Recorremos entradas
    for i in range(len(entradas)):

        # Valores
        x1 = entradas[i][0]
        x2 = entradas[i][1]
        y = salidas[i]

print(w1, w2, b)