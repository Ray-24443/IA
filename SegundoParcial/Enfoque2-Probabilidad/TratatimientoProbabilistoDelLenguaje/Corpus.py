# ---------------------------------------------
# MODELO PROBABILISTICO DEL LENGUAJE: CORPUS
# ---------------------------------------------

# Lista que representa un pequeño corpus de texto
corpus = [
    "el gato come pescado",
    "el perro come carne",
    "el gato duerme",
    "el perro corre"
]

# Diccionario para almacenar frecuencias de palabras
frecuencias = {}

# Variable para contar el total de palabras
total_palabras = 0

# Recorrer cada oración del corpus
for oracion in corpus:

    # Separar palabras
    palabras = oracion.split()

    # Recorrer cada palabra
    for palabra in palabras:

        # Aumentar contador total
        total_palabras += 1

        # Verificar si existe en el diccionario
        if palabra in frecuencias:

            # Incrementar frecuencia
            frecuencias[palabra] += 1

        else:

            # Crear nueva entrada
            frecuencias[palabra] = 1

# Mostrar frecuencias
print("Frecuencia de palabras:")
print(frecuencias)

# Mostrar probabilidades
print("\nProbabilidades:")

# Recorrer diccionario
for palabra in frecuencias:

    # Calcular probabilidad
    probabilidad = frecuencias[palabra] / total_palabras

    # Mostrar resultado
    print(palabra, "->", probabilidad)

# ----------------------------
# GRAFO SIMPLE DEL CORPUS
# ----------------------------

print("\nGrafo de relaciones:")

# Relación entre palabras
print("gato ---> come")
print("perro ---> come")
print("come ---> pescado")
print("come ---> carne")