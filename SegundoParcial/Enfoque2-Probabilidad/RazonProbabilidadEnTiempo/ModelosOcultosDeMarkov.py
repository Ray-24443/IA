# -----------------------------------------------------------
# MODELO OCULTO DE MARKOV
# -----------------------------------------------------------

# Importamos matplotlib
import matplotlib.pyplot as plt

# Estados ocultos
estados = ["Feliz", "Triste"]

# Observaciones
observaciones = ["Sonrie", "Llora"]

# Probabilidades iniciales
inicio = {
    "Feliz": 0.8,
    "Triste": 0.2
}

# Transiciones
transicion = {
    "Feliz": {
        "Feliz": 0.7,
        "Triste": 0.3
    },
    "Triste": {
        "Feliz": 0.4,
        "Triste": 0.6
    }
}

# Emisiones
emision = {
    "Feliz": {
        "Sonrie": 0.9,
        "Llora": 0.1
    },
    "Triste": {
        "Sonrie": 0.2,
        "Llora": 0.8
    }
}

# Secuencia observada
secuencia = ["Sonrie", "Llora", "Sonrie"]

# Variable de probabilidades
probabilidades = inicio.copy()

# Recorremos observaciones
for observacion in secuencia:

    # Nuevo diccionario
    nuevo = {}

    # Recorremos estados actuales
    for estado_actual in estados:

        # Inicializamos suma
        suma = 0

        # Recorremos estados anteriores
        for estado_anterior in estados:

            # Aplicamos transición
            suma += (
                probabilidades[estado_anterior]
                * transicion[estado_anterior][estado_actual]
            )

        # Multiplicamos emisión
        nuevo[estado_actual] = (
            suma
            * emision[estado_actual][observacion]
        )

    # Actualizamos probabilidades
    probabilidades = nuevo

# -----------------------------------------------------------
# RESULTADOS
# -----------------------------------------------------------

print("\n--- RESULTADOS HMM ---")

# Mostramos probabilidades finales
for estado in probabilidades:

    print(estado, ":", probabilidades[estado])

# -----------------------------------------------------------
# GRAFO HMM
# -----------------------------------------------------------

# Creamos figura
plt.figure(figsize=(8, 5))

# Estados ocultos
plt.scatter(2, 3, s=2500)
plt.scatter(6, 3, s=2500)

# Observaciones
plt.scatter(2, 1, s=2000)
plt.scatter(6, 1, s=2000)

# Etiquetas
plt.text(2, 3, "Feliz", ha='center')
plt.text(6, 3, "Triste", ha='center')

plt.text(2, 1, "Sonrie", ha='center')
plt.text(6, 1, "Llora", ha='center')

# Flechas ocultas
plt.annotate("", xy=(5.2,3), xytext=(2.8,3),
             arrowprops=dict(arrowstyle="->"))

# Flechas emisiones
plt.annotate("", xy=(2,1.5), xytext=(2,2.5),
             arrowprops=dict(arrowstyle="->"))

plt.annotate("", xy=(6,1.5), xytext=(6,2.5),
             arrowprops=dict(arrowstyle="->"))

# Título
plt.title("Modelo Oculto de Markov")

# Ocultamos ejes
plt.axis("off")

# Mostramos
plt.show()