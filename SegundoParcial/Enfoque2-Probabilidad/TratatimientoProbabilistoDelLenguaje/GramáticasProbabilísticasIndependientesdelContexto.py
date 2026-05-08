# -----------------------------------------------------
# GRAMATICAS PROBABILISTICAS INDEPENDIENTES DEL CONTEXTO
# -----------------------------------------------------

# Diccionario que representa reglas probabilísticas
gramatica = {

    # Regla inicial
    "S": [("NP VP", 1.0)],

    # Sintagma nominal
    "NP": [("gato", 0.5), ("perro", 0.5)],

    # Sintagma verbal
    "VP": [("come", 0.6), ("corre", 0.4)]
}

# Mostrar gramática
print("Gramática Probabilística:\n")

# Recorrer reglas
for regla in gramatica:

    # Mostrar nombre de regla
    print(regla)

    # Recorrer producciones
    for produccion, probabilidad in gramatica[regla]:

        # Mostrar producción
        print("  ->", produccion, " Prob:", probabilidad)

# ----------------------------
# EJEMPLO DE GENERACION
# ----------------------------

# Seleccionar producción manualmente
frase = "gato come"

# Mostrar frase
print("\nFrase generada:")
print(frase)

# ----------------------------
# GRAFO DE DERIVACION
# ----------------------------

print("\nGrafo:")

print("        S")
print("      /   \\")
print("    NP     VP")
print("    |       |")
print("  gato    come")