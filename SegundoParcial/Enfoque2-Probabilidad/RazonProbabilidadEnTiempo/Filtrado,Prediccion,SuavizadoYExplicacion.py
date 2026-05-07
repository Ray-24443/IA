# -----------------------------------------------------------
# FILTRADO, PREDICCION, SUAVIZADO Y EXPLICACION
# -----------------------------------------------------------

# Importamos matplotlib para dibujar el grafo
import matplotlib.pyplot as plt

# -----------------------------------------------------------
# DATOS DEL SISTEMA
# -----------------------------------------------------------

# Estados posibles del sistema
estados = ["Soleado", "Lluvioso"]

# Probabilidad inicial de cada estado
probabilidad_inicial = {
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

# Evidencias observadas
observaciones = ["Paraguas", "No Paraguas"]

# Probabilidades de observación
sensor = {
    "Soleado": {
        "Paraguas": 0.2,
        "No Paraguas": 0.8
    },
    "Lluvioso": {
        "Paraguas": 0.9,
        "No Paraguas": 0.1
    }
}

# Evidencia recibida
evidencia = "Paraguas"

# -----------------------------------------------------------
# FUNCION DE NORMALIZACION
# -----------------------------------------------------------

# Funcion para normalizar probabilidades
def normalizar(distribucion):

    # Sumamos todas las probabilidades
    total = sum(distribucion.values())

    # Recorremos cada estado
    for estado in distribucion:

        # Dividimos entre el total
        distribucion[estado] = distribucion[estado] / total

    # Regresamos la distribucion normalizada
    return distribucion

# -----------------------------------------------------------
# FILTRADO
# -----------------------------------------------------------

# Diccionario para guardar resultados del filtrado
filtrado = {}

# Recorremos todos los estados posibles
for estado_actual in estados:

    # Variable acumuladora
    suma = 0

    # Recorremos estados anteriores
    for estado_anterior in estados:

        # Aplicamos probabilidad de transición
        suma += (
            transicion[estado_anterior][estado_actual]
            * probabilidad_inicial[estado_anterior]
        )

    # Multiplicamos por la evidencia
    filtrado[estado_actual] = (
        sensor[estado_actual][evidencia]
        * suma
    )

# Normalizamos
filtrado = normalizar(filtrado)

# -----------------------------------------------------------
# PREDICCION
# -----------------------------------------------------------

# Diccionario para predicción
prediccion = {}

# Recorremos estados futuros
for estado_futuro in estados:

    # Variable acumuladora
    suma = 0

    # Recorremos estados actuales
    for estado_actual in estados:

        # Calculamos transición
        suma += (
            transicion[estado_actual][estado_futuro]
            * filtrado[estado_actual]
        )

    # Guardamos resultado
    prediccion[estado_futuro] = suma

# -----------------------------------------------------------
# SUAVIZADO
# -----------------------------------------------------------

# Diccionario para suavizado
suavizado = {}

# Recorremos estados
for estado in estados:

    # Multiplicamos filtrado y predicción
    suavizado[estado] = (
        filtrado[estado]
        * prediccion[estado]
    )

# Normalizamos
suavizado = normalizar(suavizado)

# -----------------------------------------------------------
# EXPLICACION
# -----------------------------------------------------------

# Buscamos el estado más probable
estado_mas_probable = max(
    suavizado,
    key=suavizado.get
)

# -----------------------------------------------------------
# RESULTADOS
# -----------------------------------------------------------

print("\n--- FILTRADO ---")
print(filtrado)

print("\n--- PREDICCION ---")
print(prediccion)

print("\n--- SUAVIZADO ---")
print(suavizado)

print("\n--- EXPLICACION ---")
print("Estado más probable:", estado_mas_probable)

# -----------------------------------------------------------
# GRAFO DEL SISTEMA
# -----------------------------------------------------------

# Creamos figura
plt.figure(figsize=(8, 5))

# Dibujamos estados
plt.scatter(1, 2, s=3000)
plt.scatter(5, 2, s=3000)

# Texto estados
plt.text(1, 2, "Soleado", ha='center', va='center')
plt.text(5, 2, "Lluvioso", ha='center', va='center')

# Flechas de transición
plt.annotate(
    "",
    xy=(4.3, 2),
    xytext=(1.7, 2),
    arrowprops=dict(arrowstyle="->")
)

plt.annotate(
    "",
    xy=(1.7, 1.7),
    xytext=(4.3, 1.7),
    arrowprops=dict(arrowstyle="->")
)

# Texto probabilidades
plt.text(3, 2.2, "0.3")
plt.text(3, 1.5, "0.4")

# Título
plt.title("Grafo de Estados")

# Quitamos ejes
plt.axis("off")

# Mostramos
plt.show()