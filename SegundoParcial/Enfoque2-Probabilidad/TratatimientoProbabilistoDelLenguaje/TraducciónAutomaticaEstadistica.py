# -----------------------------------------
# TRADUCCION AUTOMATICA ESTADISTICA
# -----------------------------------------

# Diccionario de traducción
diccionario = {

    "hola": "hello",
    "mundo": "world",
    "gato": "cat",
    "perro": "dog"
}

# Frase en español
frase_es = "hola mundo"

# Separar palabras
palabras = frase_es.split()

# Lista para traducción
traduccion = []

# Recorrer palabras
for palabra in palabras:

    # Verificar si existe en diccionario
    if palabra in diccionario:

        # Agregar traducción
        traduccion.append(diccionario[palabra])

# Unir traducción
frase_en = " ".join(traduccion)

# Mostrar resultado
print("Frase original:")
print(frase_es)

print("\nTraducción:")
print(frase_en)

# ----------------------------
# GRAFO DE TRADUCCION
# ----------------------------

print("\nGrafo:")

print("Español ---> Modelo Estadístico ---> Inglés")
print("hola ---> hello")
print("mundo ---> world")