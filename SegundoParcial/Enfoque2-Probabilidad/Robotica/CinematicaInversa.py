# ---------------------------------------------------------
# CINEMATICA INVERSA
# ---------------------------------------------------------

# Importamos math
import math

# Longitud del brazo 1
l1 = 10

# Longitud del brazo 2
l2 = 10

# Punto objetivo
x = 10
y = 10

# Calculamos distancia
distancia = math.sqrt((x ** 2) + (y ** 2))

# Calculamos ángulo 2
angulo2 = math.acos(
    ((distancia ** 2) - (l1 ** 2) - (l2 ** 2)) /
    (2 * l1 * l2)
)

# Convertimos a grados
angulo2_grados = math.degrees(angulo2)

# Mostramos resultado
print("Angulo 2:", angulo2_grados)