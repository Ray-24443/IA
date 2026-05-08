# ==========================================
# MODELO DE MARKOV OCULTO (HMM)
# ==========================================

# Estados ocultos
estados = ["Soleado", "Lluvioso"]

# Observaciones visibles
observaciones = ["Caminar", "Comprar", "Limpiar"]

# Probabilidades iniciales
prob_inicial = {
    "Soleado": 0.6,
    "Lluvioso": 0.4
}

# Probabilidades de transición
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

# Probabilidades de emisión
emision = {
    "Soleado": {
        "Caminar": 0.6,
        "Comprar": 0.3,
        "Limpiar": 0.1
    },
    "Lluvioso": {
        "Caminar": 0.1,
        "Comprar": 0.4,
        "Limpiar": 0.5
    }
}

# Secuencia observada
secuencia = ["Caminar", "Comprar", "Limpiar"]

# Matriz de probabilidades
V = [{}]

# ------------------------------------------
# Inicialización
# ------------------------------------------
for estado in estados:

    # Probabilidad inicial
    V[0][estado] = (
        prob_inicial[estado]
        * emision[estado][secuencia[0]]
    )

# ------------------------------------------
# Algoritmo de Viterbi
# ------------------------------------------
for t in range(1, len(secuencia)):

    # Agregamos nuevo tiempo
    V.append({})

    # Recorremos estados
    for estado in estados:

        # Lista temporal
        probabilidades = []

        # Revisamos estados anteriores
        for estado_anterior in estados:

            # Calculamos probabilidad
            probabilidad = (
                V[t - 1][estado_anterior]
                * transicion[estado_anterior][estado]
                * emision[estado][secuencia[t]]
            )

            # Guardamos
            probabilidades.append(probabilidad)

        # Guardamos máxima probabilidad
        V[t][estado] = max(probabilidades)

# ------------------------------------------
# Mostrar resultados
# ------------------------------------------
print("Resultados del HMM:\n")

for tiempo in range(len(V)):
    print("Tiempo", tiempo)
    print(V[tiempo])