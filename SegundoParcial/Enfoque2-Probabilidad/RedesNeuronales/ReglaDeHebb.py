# ==========================================
# REGLA DE HEBB
# ==========================================

# Entradas
x1 = 1
x2 = 1

# Salida
y = 1

# Pesos
w1 = 0
w2 = 0

# Aprendizaje Hebb
w1 = w1 + (x1 * y)
w2 = w2 + (x2 * y)

# Resultado
print(w1, w2)