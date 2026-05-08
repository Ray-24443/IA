# -------------------------------------------------
# DETECCION DE ARISTAS Y SEGMENTACION
# -------------------------------------------------

# Crear imagen sencilla
imagen = [

    [10, 10, 10, 10],
    [10, 90, 90, 10],
    [10, 90, 90, 10],
    [10, 10, 10, 10]
]

# Mostrar imagen original
print("Imagen original:\n")

# Recorrer filas
for fila in imagen:

    # Mostrar fila
    print(fila)

# Crear lista de bordes
bordes = []

# Recorrer filas internas
for i in range(1, 3):

    # Crear fila temporal
    fila_borde = []

    # Recorrer columnas internas
    for j in range(1, 3):

        # Calcular diferencia horizontal
        diferencia = abs(imagen[i][j] - imagen[i][j-1])

        # Verificar borde
        if diferencia > 20:

            # Detectar borde
            fila_borde.append(1)

        else:

            # No hay borde
            fila_borde.append(0)

    # Agregar fila
    bordes.append(fila_borde)

# Mostrar bordes
print("\nAristas detectadas:\n")

# Recorrer filas
for fila in bordes:

    # Mostrar fila
    print(fila)

# -------------------------------------------------
# SEGMENTACION SIMPLE
# -------------------------------------------------

print("\nSegmentacion:\n")

# Recorrer imagen
for fila in imagen:

    # Lista temporal
    nueva = []

    # Recorrer valores
    for valor in fila:

        # Clasificar región clara
        if valor > 50:

            nueva.append(1)

        else:

            nueva.append(0)

    # Mostrar región segmentada
    print(nueva)

# -------------------------------------------------
# EJEMPLO
# -------------------------------------------------
# Los valores altos representan un objeto separado