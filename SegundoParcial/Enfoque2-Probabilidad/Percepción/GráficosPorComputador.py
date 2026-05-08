# -------------------------------------------------
# GRAFICOS POR COMPUTADOR
# DIBUJO SIMPLE DE UNA FIGURA EN MATRIZ
# -------------------------------------------------

# Crear matriz vacía de 10x10
pantalla = []

# Crear filas
for i in range(10):

    # Crear fila llena de espacios
    fila = []

    # Crear columnas
    for j in range(10):

        # Agregar espacio vacío
        fila.append(".")

    # Agregar fila a pantalla
    pantalla.append(fila)

# Dibujar un cuadrado
for i in range(3, 7):

    # Dibujar línea izquierda
    pantalla[i][3] = "#"

    # Dibujar línea derecha
    pantalla[i][6] = "#"

# Dibujar líneas horizontales
for j in range(3, 7):

    # Línea superior
    pantalla[3][j] = "#"

    # Línea inferior
    pantalla[6][j] = "#"

# Mostrar pantalla
print("Grafico generado:\n")

# Recorrer filas
for fila in pantalla:

    # Convertir fila en texto
    print(" ".join(fila))

# -------------------------------------------------
# EJEMPLO DEL RESULTADO
# -------------------------------------------------
# Debe aparecer un cuadrado formado con #