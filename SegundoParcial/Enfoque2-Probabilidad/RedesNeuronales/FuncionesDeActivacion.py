# ==========================================
# FUNCIONES DE ACTIVACIÓN
# ==========================================

# Importamos math
import math

# Valor de prueba
x = 1.5

# Función escalón
if x >= 0:
    escalon = 1
else:
    escalon = 0

# Función sigmoide
sigmoide = 1 / (1 + math.exp(-x))

# Función tanh
tanh = math.tanh(x)

# Función ReLU
if x > 0:
    relu = x
else:
    relu = 0

# Resultados
print("Escalón:", escalon)
print("Sigmoide:", sigmoide)
print("Tanh:", tanh)
print("ReLU:", relu)