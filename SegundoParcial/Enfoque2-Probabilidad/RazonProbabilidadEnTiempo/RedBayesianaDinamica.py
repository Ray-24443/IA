# -----------------------------------------------------------
# FILTRADO DE PARTICULAS
# -----------------------------------------------------------

# Importamos librerías
import random
import matplotlib.pyplot as plt

# Número de partículas
numero_particulas = 100

# Creamos partículas aleatorias
particulas = []

# Generamos partículas
for i in range(numero_particulas):

    particulas.append(random.randint(0, 10))

# Observación real
observacion = 7

# Lista pesos
pesos = []

# -----------------------------------------------------------
# CALCULO DE PESOS
# -----------------------------------------------------------

# Recorremos partículas
for particula in particulas:

    # Distancia respecto observación
    distancia = abs(observacion - particula)

    # Peso inversamente proporcional
    peso = 1 / (distancia + 1)

    # Guardamos peso
    pesos.append(peso)

# -----------------------------------------------------------
# NORMALIZACION
# -----------------------------------------------------------

# Suma total
suma_pesos = sum(pesos)

# Lista normalizada
pesos_normalizados = []

# Recorremos pesos
for peso in pesos:

    pesos_normalizados.append(peso / suma_pesos)

# -----------------------------------------------------------
# REMUESTREO
# -----------------------------------------------------------

# Nuevas partículas
nuevas_particulas = []

# Generamos nuevas partículas
for i in range(numero_particulas):

    # Elegimos partícula según peso
    seleccion = random.choices(
        particulas,
        weights=pesos_normalizados
    )[0]

    # Guardamos
    nuevas_particulas.append(seleccion)

# -----------------------------------------------------------
# RESULTADOS
# -----------------------------------------------------------

print("\n--- PARTICULAS ORIGINALES ---")
print(particulas)

print("\n--- PARTICULAS REMUESTREADAS ---")
print(nuevas_particulas)

# -----------------------------------------------------------
# GRAFICA
# -----------------------------------------------------------

# Creamos figura
plt.figure(figsize=(10, 5))

# Histograma inicial
plt.hist(
    particulas,
    bins=11,
    alpha=0.5,
    label="Originales"
)

# Histograma final
plt.hist(
    nuevas_particulas,
    bins=11,
    alpha=0.5,
    label="Remuestreadas"
)

# Línea observación
plt.axvline(observacion, linestyle='--', label="Observacion")

# Título
plt.title("Filtrado de Particulas")

# Leyenda
plt.legend()

# Mostramos
plt.show()