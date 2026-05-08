# ==========================================
# MAPA DE KOHONEN
# ==========================================

# Datos
entradas = [1, 2, 8, 9]

# Neuronas
neuronas = [2, 7]

# Recorremos entradas
for entrada in entradas:

    # Distancias
    distancias = []

    # Recorremos neuronas
    for neurona in neuronas:

        # Distancia
        distancia = abs(entrada - neurona)

        # Guardamos
        distancias.append(distancia)

    # Neurona ganadora
    ganador = distancias.index(min(distancias))

    # Ajustamos neurona
    neuronas[ganador] = neuronas[ganador] + 0.5 * (entrada - neuronas[ganador])

    # Mostramos
    print(neuronas)