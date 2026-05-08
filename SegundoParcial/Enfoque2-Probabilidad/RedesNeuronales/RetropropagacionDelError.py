# ==========================================
# RETROPROPAGACIÓN
# ==========================================

# Error inicial
error = 0.8

# Learning rate
lr = 0.1

# Peso inicial
peso = 0.5

# Iteraciones
for i in range(10):

    # Ajuste
    peso = peso - (lr * error)

    # Reducimos error
    error = error * 0.8

    # Mostramos valores
    print(peso, error)