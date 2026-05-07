# -----------------------------------------------------------
# AGRUPAMIENTO NO SUPERVISADO
# -----------------------------------------------------------

# -----------------------------------------------------------
# DATOS
# -----------------------------------------------------------

# Lista de puntos
puntos = [1, 2, 3, 8, 9, 10]

# Centro inicial 1
centro1 = 2

# Centro inicial 2
centro2 = 9

# Número de iteraciones
iteraciones = 5

# -----------------------------------------------------------
# ALGORITMO K-MEANS SIMPLE
# -----------------------------------------------------------

# Repetimos iteraciones
for iteracion in range(iteraciones):

    # Lista cluster 1
    cluster1 = []

    # Lista cluster 2
    cluster2 = []

    # -------------------------------------------------------
    # ASIGNACION DE CLUSTERS
    # -------------------------------------------------------

    # Recorremos puntos
    for punto in puntos:

        # Distancia al centro1
        distancia1 = abs(punto - centro1)

        # Distancia al centro2
        distancia2 = abs(punto - centro2)

        # Verificamos distancia mínima
        if distancia1 < distancia2:

            # Agregamos a cluster1
            cluster1.append(punto)

        else:

            # Agregamos a cluster2
            cluster2.append(punto)

    # -------------------------------------------------------
    # ACTUALIZACION DE CENTROS
    # -------------------------------------------------------

    # Nuevo centro1
    centro1 = sum(cluster1) / len(cluster1)

    # Nuevo centro2
    centro2 = sum(cluster2) / len(cluster2)

    # -------------------------------------------------------
    # RESULTADOS
    # -------------------------------------------------------

    # Mostramos iteración
    print("\nIteración:", iteracion + 1)

    # Mostramos cluster1
    print("Cluster 1:", cluster1)

    # Mostramos cluster2
    print("Cluster 2:", cluster2)

    # Mostramos centro1
    print("Centro 1:", centro1)

    # Mostramos centro2
    print("Centro 2:", centro2)

# -----------------------------------------------------------
# RESULTADO FINAL
# -----------------------------------------------------------

# Mostramos encabezado
print("\n--- AGRUPAMIENTO FINAL ---")

# Resultado cluster1
print("Cluster 1 final:", cluster1)

# Resultado cluster2
print("Cluster 2 final:", cluster2)

# -----------------------------------------------------------
# GRAFO SIMPLE
# -----------------------------------------------------------

# Representación textual
print("\nGRAFO:")

# Relación de clusters
print("Puntos ---> Cluster 1")
print("       ---> Cluster 2")