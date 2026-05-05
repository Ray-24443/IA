# Variable aleatoria: resultado de un dado
valores = [1, 2, 3, 4, 5, 6]  # Posibles resultados

# Distribución uniforme
probabilidades = {}  # Diccionario vacío

# Asignamos probabilidad igual
for valor in valores:  # Recorremos valores
    probabilidades[valor] = 1/6  # Cada uno tiene misma probabilidad

# Verificamos suma
suma = 0  # Inicializamos suma

for valor in probabilidades:  # Recorremos
    suma += probabilidades[valor]  # Sumamos

# Mostrar resultados
print("Distribución:", probabilidades)
print("Suma total:", suma)  # Debe ser 1