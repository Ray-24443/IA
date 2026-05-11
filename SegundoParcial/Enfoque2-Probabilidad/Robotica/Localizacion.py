# ---------------------------------------------------------
# LOCALIZACION MONTE-CARLO
# ---------------------------------------------------------

# Importamos random
import random

# Lista de partículas
particulas = []

# Generamos 10 partículas aleatorias
for i in range(10):

    # Posición aleatoria entre 0 y 100
    posicion = random.randint(0, 100)

    # Agregamos partícula
    particulas.append(posicion)

# Mostramos partículas iniciales
print("Particulas iniciales:")
print(particulas)

# Simulamos medición real
medicion_real = 60

# Lista de partículas válidas
particulas_validas = []

# Recorremos partículas
for p in particulas:

    # Verificamos cercanía a medición
    if abs(p - medicion_real) < 20:

        # Guardamos partícula válida
        particulas_validas.append(p)

# Mostramos partículas filtradas
print("Particulas cercanas:")
print(particulas_validas)