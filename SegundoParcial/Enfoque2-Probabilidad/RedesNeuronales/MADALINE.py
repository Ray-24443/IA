# ==========================================
# MADALINE
# ==========================================

# Entradas
x1 = 1
x2 = 0

# Pesos primera capa
w1 = 0.5
w2 = -0.3

# Pesos segunda capa
w3 = 0.8
w4 = 0.2

# Neurona 1
n1 = (x1 * w1) + (x2 * w2)

# Neurona 2
n2 = (x1 * w3) + (x2 * w4)

# Activaciones
if n1 >= 0:
    s1 = 1
else:
    s1 = 0

if n2 >= 0:
    s2 = 1
else:
    s2 = 0

# Salida final
salida = s1 + s2

print(salida)