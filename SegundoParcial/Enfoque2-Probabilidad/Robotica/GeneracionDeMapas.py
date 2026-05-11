# ---------------------------------------------------------
# SLAM - GENERACION DE MAPAS
# ---------------------------------------------------------

# Creamos mapa vacío de 10x10
mapa = []

# Generamos filas
for i in range(10):

    # Creamos fila vacía
    fila = []

    # Generamos columnas
    for j in range(10):

        # Agregamos espacio libre
        fila.append(".")

    # Guardamos fila
    mapa.append(fila)

# Posición del robot
x = 5
y = 5
    
# Colocamos robot en mapa
mapa[y][x] = "R"

# Colocamos obstáculos
mapa[2][3] = "X"
mapa[7][8] = "X"

# Mostramos mapa
for fila in mapa:

    # Imprimimos fila
    print(" ".join(fila))