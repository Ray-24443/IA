# ---------------------------------------------------------
# ESPACIO DE CONFIGURACION
# ---------------------------------------------------------

# Lista de posiciones posibles
posiciones = []

# Generamos posiciones
for x in range(5):

    # Generamos posiciones en y
    for y in range(5):

        # Guardamos coordenadas
        posiciones.append((x, y))

# Mostramos posiciones
print("Espacio de configuracion:")
print(posiciones)