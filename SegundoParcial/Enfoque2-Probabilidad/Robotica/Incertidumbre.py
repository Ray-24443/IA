# ---------------------------------------------------------
# INCERTIDUMBRE
# ---------------------------------------------------------

# Importamos random
import random

# Generamos mediciones
mediciones = []

# Creamos 10 datos aleatorios
for i in range(10):

    # Número entre 90 y 110
    dato = random.randint(90, 110)

    # Guardamos dato
    mediciones.append(dato)

# Mostramos mediciones
print("Mediciones:")
print(mediciones)

# Calculamos promedio
promedio = sum(mediciones) / len(mediciones)

# Mostramos promedio
print("Promedio:", promedio)