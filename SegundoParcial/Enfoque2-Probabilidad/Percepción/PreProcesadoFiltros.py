# -------------------------------------------------
# PREPROCESADO: FILTRO PROMEDIO
# -------------------------------------------------

# Crear imagen de ejemplo
imagen = [

    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Mostrar imagen original
print("Imagen original:\n")

# Recorrer filas
for fila in imagen:

    # Mostrar fila
    print(fila)

# Crear nueva imagen filtrada
filtrada = []

# Recorrer filas internas
for i in range(1, 2):

    # Crear fila temporal
    fila_temp = []

    # Recorrer columnas internas
    for j in range(1, 2):

        # Sumar vecinos
        suma = (
            imagen[i-1][j-1] +
            imagen[i-1][j] +
            imagen[i-1][j+1] +
            imagen[i][j-1] +
            imagen[i][j] +
            imagen[i][j+1] +
            imagen[i+1][j-1] +
            imagen[i+1][j] +
            imagen[i+1][j+1]
        )

        # Calcular promedio
        promedio = suma / 9

        # Agregar promedio
        fila_temp.append(promedio)

    # Agregar fila
    filtrada.append(fila_temp)

# Mostrar imagen filtrada
print("\nImagen filtrada:\n")

# Recorrer filas
for fila in filtrada:

    # Mostrar fila
    print(fila)

# -------------------------------------------------
# EJEMPLO
# -------------------------------------------------
# El valor central será suavizado mediante promedio