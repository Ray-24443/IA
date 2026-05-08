# -----------------------------------------
# EXTRACCION DE INFORMACION
# -----------------------------------------

# Texto de ejemplo
texto = "Juan estudia Python en Guadalajara"

# Separar palabras
palabras = texto.split()

# Variables
nombre = ""
lenguaje = ""
ciudad = ""

# Recorrer palabras
for palabra in palabras:

    # Detectar nombre
    if palabra == "Juan":

        nombre = palabra

    # Detectar lenguaje
    if palabra == "Python":

        lenguaje = palabra

    # Detectar ciudad
    if palabra == "Guadalajara":

        ciudad = palabra

# Mostrar resultados
print("Nombre:", nombre)
print("Lenguaje:", lenguaje)
print("Ciudad:", ciudad)

# ----------------------------
# GRAFO
# ----------------------------

print("\nGrafo:")

print("Texto ---> Procesamiento")
print("Procesamiento ---> Nombre")
print("Procesamiento ---> Lenguaje")
print("Procesamiento ---> Ciudad")