# ==========================================
# K-MEANS
# ==========================================

# Importamos random
import random

# Puntos
puntos = [
    [1, 2],
    [2, 1],
    [1, 1],
    [8, 8],
    [9, 8],
    [8, 9]
]

# Número de clusters
k = 2

# Centroides iniciales
centroides = random.sample(puntos, k)

# Iteraciones
for iteracion in range(5):

    # Clusters vacíos
    clusters = [[], []]

    # Recorremos puntos
    for punto in puntos:

        # Lista de distancias
        distancias = []

        # Recorremos centroides
        for centroide in centroides:

            # Distancia
            dx = punto[0] - centroide[0]
            dy = punto[1] - centroide[1]

            distancia = (dx * dx + dy * dy) ** 0.5

            # Guardamos distancia
            distancias.append(distancia)

        # Centroide más cercano
        indice = distancias.index(min(distancias))

        # Guardamos punto
        clusters[indice].append(punto)

    # Nuevos centroides
    nuevos_centroides = []

    # Recorremos clusters
    for cluster in clusters:

        # Promedio x
        promedio_x = sum(p[0] for p in cluster) / len(cluster)

        # Promedio y
        promedio_y = sum(p[1] for p in cluster) / len(cluster)

        # Guardamos centroide
        nuevos_centroides.append([promedio_x, promedio_y])

    # Actualizamos centroides
    centroides = nuevos_centroides

# Resultado
print(clusters)