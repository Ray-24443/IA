# -----------------------------------------------------------
# APRENDIZAJE BAYESIANO
# -----------------------------------------------------------

# Importamos librería matemática
import math

# -----------------------------------------------------------
# DATOS
# -----------------------------------------------------------

# Probabilidad previa de aprobar
prob_aprobar = 0.6

# Probabilidad previa de reprobar
prob_reprobar = 0.4

# Probabilidad de estudiar si aprueba
prob_estudiar_aprobar = 0.8

# Probabilidad de estudiar si reprueba
prob_estudiar_reprobar = 0.3

# Evidencia observada
evidencia_estudiar = (
    (prob_estudiar_aprobar * prob_aprobar)
    +
    (prob_estudiar_reprobar * prob_reprobar)
)

# -----------------------------------------------------------
# TEOREMA DE BAYES
# -----------------------------------------------------------

# Calculamos probabilidad posterior
probabilidad_posterior = (
    (prob_estudiar_aprobar * prob_aprobar)
    /
    evidencia_estudiar
)

# -----------------------------------------------------------
# RESULTADOS
# -----------------------------------------------------------

# Mostramos resultados
print("\n--- APRENDIZAJE BAYESIANO ---")

# Imprimimos probabilidad posterior
print(
    "Probabilidad de aprobar dado que estudia:",
    round(probabilidad_posterior, 4)
)

# -----------------------------------------------------------
# GRAFO SIMPLE
# -----------------------------------------------------------

# Imprimimos representación del modelo
print("\nGRAFO:")

# Nodo principal
print("Estudiar ---> Aprobar")