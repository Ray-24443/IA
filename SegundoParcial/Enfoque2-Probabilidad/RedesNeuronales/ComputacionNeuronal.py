# ==========================================
# COMPUTACIÓN NEURONAL
# ==========================================

# Entradas
x1 = 1
x2 = 0

# Pesos
w1 = 0.7
w2 = 0.5

# Bias
b = -0.2

# Suma ponderada
suma = (x1 * w1) + (x2 * w2) + b

# Activación
if suma >= 0:
    salida = 1
else:
    salida = 0

# Resultado
print("Salida neuronal:")
print(salida)