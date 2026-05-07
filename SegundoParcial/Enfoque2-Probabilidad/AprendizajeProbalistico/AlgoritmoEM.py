# -----------------------------------------------------------
# ALGORITMO EM
# -----------------------------------------------------------

# Importamos librería random
import random

# -----------------------------------------------------------
# DATOS
# -----------------------------------------------------------

# Datos observados
datos = [1, 2, 3, 8, 9, 10]

# Media inicial grupo 1
media1 = 2

# Media inicial grupo 2
media2 = 9

# Número de iteraciones
iteraciones = 5

# -----------------------------------------------------------
# INICIO DEL ALGORITMO
# -----------------------------------------------------------

# Repetimos varias iteraciones
for iteracion in range(iteraciones):

    # Lista grupo 1
    grupo1 = []

    # Lista grupo 2
    grupo2 = []

    # -------------------------------------------------------
    # PASO E
    # -------------------------------------------------------

    # Recorremos datos
    for dato in datos:

        # Distancia a media1
        distancia1 = abs(dato - media1)

        # Distancia a media2
        distancia2 = abs(dato - media2)

        # Verificamos grupo más cercano
        if distancia1 < distancia2:

            # Guardamos en grupo1
            grupo1.append(dato)

        else:

            # Guardamos en grupo2
            grupo2.append(dato)

    # -------------------------------------------------------
    # PASO M
    # -------------------------------------------------------

    # Actualizamos media1
    media1 = sum(grupo1) / len(grupo1)

    # Actualizamos media2
    media2 = sum(grupo2) / len(grupo2)

    # -------------------------------------------------------
    # RESULTADOS ITERACION
    # -------------------------------------------------------

    # Mostramos iteración
    print("\nIteración:", iteracion + 1)

    # Mostramos grupo1
    print("Grupo 1:", grupo1)

    # Mostramos grupo2
    print("Grupo 2:", grupo2)

    # Mostramos medias
    print("Media 1:", media1)

    # Mostramos medias
    print("Media 2:", media2)

# -----------------------------------------------------------
# GRAFO SIMPLE
# -----------------------------------------------------------

# Mostramos grafo
print("\nGRAFO:")

# Representación del proceso
print("Datos --> Paso E --> Paso M --> Nuevas Medias")