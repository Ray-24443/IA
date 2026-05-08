# -------------------------------------------------
# TEXTURAS Y SOMBRAS
# -------------------------------------------------

# Crear matriz de textura
textura = [

    [1, 2, 1, 2],
    [2, 1, 2, 1],
    [1, 2, 1, 2],
    [2, 1, 2, 1]
]

# Mostrar textura
print("Textura:\n")

# Recorrer filas
for fila in textura:

    # Mostrar fila
    print(fila)

# -------------------------------------------------
# GENERACION DE SOMBRA
# -------------------------------------------------

# Crear lista de sombras
sombras = []

# Recorrer filas
for fila in textura:

    # Crear fila temporal
    fila_sombra = []

    # Recorrer valores
    for valor in fila:

        # Multiplicar intensidad
        sombra = valor * 30

        # Agregar sombra
        fila_sombra.append(sombra)

    # Agregar fila
    sombras.append(fila_sombra)

# Mostrar sombras
print("\nSombras generadas:\n")

# Recorrer filas
for fila in sombras:

    # Mostrar fila
    print(fila)

# -------------------------------------------------
# GRAFO DE FUNCIONAMIENTO
# -------------------------------------------------

print("\nProceso:\n")

print("Textura ---> Procesamiento ---> Sombras")