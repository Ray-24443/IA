# ==========================================
# K-NN
# ==========================================

# Importamos math
import math

# Datos de entrenamiento
# peso, tamaño, clase
datos = [
    [150, 7, "Manzana"],
    [170, 7.5, "Manzana"],
    [140, 6.8, "Manzana"],
    [120, 9, "Naranja"],
    [110, 8.7, "Naranja"]
]

# Nuevo dato
nuevo = [145, 7.2]

# Valor de k
k = 3

# Lista de distancias
distancias = []

# Recorremos datos
for dato in datos:

    # Diferencia eje x
    dx = dato[0] - nuevo[0]

    # Diferencia eje y
    dy = dato[1] - nuevo[1]

    # Distancia euclidiana
    distancia = math.sqrt(dx * dx + dy * dy)

    # Guardamos distancia y clase
    distancias.append([distancia, dato[2]])

# Ordenamos distancias
distancias.sort()

# Tomamos vecinos más cercanos
vecinos = distancias[:k]

# Contadores
manzana = 0
naranja = 0

# Recorremos vecinos
for vecino in vecinos:

    # Si es manzana
    if vecino[1] == "Manzana":
        manzana += 1

    # Si es naranja
    else:
        naranja += 1

# Resultado final
if manzana > naranja:
    print("La fruta es Manzana")
else:
    print("La fruta es Naranja")