# -----------------------------------------------------------
# ALGORITMO HACIA DELANTE - ATRAS
# -----------------------------------------------------------

# Importamos librería para graficar
import matplotlib.pyplot as plt

# Estados ocultos
estados = ["Soleado", "Lluvioso"]

# Observaciones
observaciones = ["Paraguas", "Paraguas", "No Paraguas"]

# Probabilidades iniciales
inicio = {
    "Soleado": 0.6,
    "Lluvioso": 0.4
}

# Matriz de transición
transicion = {
    "Soleado": {
        "Soleado": 0.7,
        "Lluvioso": 0.3
    },
    "Lluvioso": {
        "Soleado": 0.4,
        "Lluvioso": 0.6
    }
}

# Matriz de emisión
emision = {
    "Soleado": {
        "Paraguas": 0.2,
        "No Paraguas": 0.8
    },
    "Lluvioso": {
        "Paraguas": 0.9,
        "No Paraguas": 0.1
    }
}

# -----------------------------------------------------------
# ETAPA HACIA DELANTE
# -----------------------------------------------------------

# Lista forward
forward = []

# Primer paso
primer_paso = {}

# Recorremos estados
for estado in estados:

    # Calculamos probabilidad inicial
    primer_paso[estado] = (
        inicio[estado]
        * emision[estado][observaciones[0]]
    )

# Guardamos
forward.append(primer_paso)

# Recorremos observaciones restantes
for t in range(1, len(observaciones)):

    # Diccionario temporal
    actual = {}

    # Recorremos estados actuales
    for estado_actual in estados:

        # Inicializamos suma
        suma = 0

        # Recorremos estados anteriores
        for estado_anterior in estados:

            # Aplicamos fórmula
            suma += (
                forward[t - 1][estado_anterior]
                * transicion[estado_anterior][estado_actual]
            )

        # Multiplicamos por emisión
        actual[estado_actual] = (
            suma
            * emision[estado_actual][observaciones[t]]
        )

    # Guardamos paso
    forward.append(actual)

# -----------------------------------------------------------
# ETAPA HACIA ATRAS
# -----------------------------------------------------------

# Lista backward
backward = []

# Inicializamos último paso
ultimo = {}

# Todos inician en 1
for estado in estados:

    ultimo[estado] = 1

# Insertamos al inicio
backward.insert(0, ultimo)

# Recorremos hacia atrás
for t in range(len(observaciones) - 2, -1, -1):

    # Diccionario actual
    actual = {}

    # Recorremos estados
    for estado_actual in estados:

        # Inicializamos suma
        suma = 0

        # Recorremos estados futuros
        for estado_futuro in estados:

            # Aplicamos fórmula
            suma += (
                transicion[estado_actual][estado_futuro]
                * emision[estado_futuro][observaciones[t + 1]]
                * backward[0][estado_futuro]
            )

        # Guardamos
        actual[estado_actual] = suma

    # Insertamos al inicio
    backward.insert(0, actual)

# -----------------------------------------------------------
# RESULTADOS
# -----------------------------------------------------------

print("\n--- FORWARD ---")

# Mostramos forward
for i in range(len(forward)):

    print("Tiempo", i + 1, ":", forward[i])

print("\n--- BACKWARD ---")

# Mostramos backward
for i in range(len(backward)):

    print("Tiempo", i + 1, ":", backward[i])

# -----------------------------------------------------------
# GRAFO
# -----------------------------------------------------------

# Creamos figura
plt.figure(figsize=(10, 4))

# Coordenadas nodos
x = [1, 3, 5]
y1 = [2, 2, 2]
y2 = [1, 1, 1]

# Dibujamos estados
plt.scatter(x, y1, s=1500)
plt.scatter(x, y2, s=1500)

# Etiquetas
for i in range(3):

    plt.text(x[i], y1[i], "S", ha='center', va='center')
    plt.text(x[i], y2[i], "L", ha='center', va='center')

# Flechas
for i in range(2):

    plt.annotate("", xy=(x[i+1],2), xytext=(x[i],2),
                 arrowprops=dict(arrowstyle="->"))

    plt.annotate("", xy=(x[i+1],1), xytext=(x[i],1),
                 arrowprops=dict(arrowstyle="->"))

# Título
plt.title("Algoritmo Hacia Delante-Atrás")

# Quitamos ejes
plt.axis("off")

# Mostramos
plt.show()