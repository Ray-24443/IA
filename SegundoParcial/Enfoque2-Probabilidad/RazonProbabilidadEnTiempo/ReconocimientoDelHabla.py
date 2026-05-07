# -----------------------------------------------------------
# RECONOCIMIENTO DEL HABLA SIMPLE
# -----------------------------------------------------------

# Importamos matplotlib
import matplotlib.pyplot as plt

# Palabras conocidas
palabras = ["hola", "adios", "gracias"]

# Entrada simulada
entrada = "hola"

# Variable encontrada
resultado = "Desconocido"

# -----------------------------------------------------------
# RECONOCIMIENTO
# -----------------------------------------------------------

# Recorremos palabras
for palabra in palabras:

    # Comparamos entrada
    if entrada == palabra:

        # Guardamos coincidencia
        resultado = palabra

# -----------------------------------------------------------
# RESULTADOS
# -----------------------------------------------------------

print("\n--- RECONOCIMIENTO DEL HABLA ---")

# Mostramos entrada
print("Entrada:", entrada)

# Mostramos resultado
print("Reconocido:", resultado)

# -----------------------------------------------------------
# GRAFO
# -----------------------------------------------------------

# Creamos figura
plt.figure(figsize=(8, 4))

# Dibujamos nodos
plt.scatter(1, 2, s=2000)
plt.scatter(4, 2, s=2000)
plt.scatter(7, 2, s=2000)

# Etiquetas
plt.text(1, 2, "Audio", ha='center')
plt.text(4, 2, "Procesamiento", ha='center')
plt.text(7, 2, "Texto", ha='center')

# Flechas
plt.annotate("", xy=(3.2,2), xytext=(1.8,2),
             arrowprops=dict(arrowstyle="->"))

plt.annotate("", xy=(6.2,2), xytext=(4.8,2),
             arrowprops=dict(arrowstyle="->"))

# Título
plt.title("Proceso de Reconocimiento del Habla")

# Ocultamos ejes
plt.axis("off")

# Mostramos
plt.show()