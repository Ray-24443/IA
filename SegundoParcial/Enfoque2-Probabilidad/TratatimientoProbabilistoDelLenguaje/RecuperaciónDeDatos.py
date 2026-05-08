# -----------------------------------------
# RECUPERACION DE DATOS
# -----------------------------------------

# Lista de documentos
documentos = [

    "el gato come pescado",
    "el perro corre rapido",
    "inteligencia artificial y python",
    "el gato duerme mucho"
]

# Consulta del usuario
consulta = "gato"

# Lista para resultados
resultados = []

# Recorrer documentos
for documento in documentos:

    # Verificar si la consulta está en documento
    if consulta in documento:

        # Agregar resultado
        resultados.append(documento)

# Mostrar resultados
print("Documentos encontrados:\n")

# Recorrer resultados
for r in resultados:

    # Mostrar documento
    print(r)

# ----------------------------
# GRAFO DE RECUPERACION
# ----------------------------

print("\nGrafo:")

print("Usuario ---> Consulta")
print("Consulta ---> Base de Datos")
print("Base de Datos ---> Resultado")