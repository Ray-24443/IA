# ------------------------------------------------
# GRAMATICAS PROBABILISTICAS LEXICALIZADAS
# ------------------------------------------------

# Diccionario de reglas lexicalizadas
gramatica_lex = {

    # Regla principal
    "S": [("NP VP", 1.0)],

    # Sintagma nominal
    "NP": [("gato", 0.7), ("perro", 0.3)],

    # Sintagma verbal
    "VP": [("come pescado", 0.8), ("corre rapido", 0.2)]
}

# Mostrar reglas
print("Gramática Lexicalizada:\n")

# Recorrer reglas
for regla in gramatica_lex:

    # Mostrar regla
    print(regla)

    # Recorrer producciones
    for produccion, probabilidad in gramatica_lex[regla]:

        # Mostrar producción
        print(" ->", produccion, " Prob:", probabilidad)

# ----------------------------
# GENERACION DE FRASE
# ----------------------------

# Crear frase de ejemplo
frase = "gato come pescado"

# Mostrar frase
print("\nFrase:")
print(frase)

# ----------------------------
# GRAFO
# ----------------------------

print("\nGrafo:")

print("S")
print("|")
print("NP ---- VP")
print("|       |")
print("gato   come pescado")