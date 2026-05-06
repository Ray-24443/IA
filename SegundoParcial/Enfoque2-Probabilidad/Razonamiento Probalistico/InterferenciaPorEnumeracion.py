# =========================================
# INFERENCIA POR ENUMERACIÓN
# =========================================

# -----------------------------------------
# RED BAYESIANA (EJEMPLO INCLUIDO)
# -----------------------------------------
# Definimos una red simple
red = {
    "Lluvia": {
        "padres": [],  # No depende de ninguna variable
        "cpt": {True: 0.2, False: 0.8}  # Probabilidad directa
    },
    "Aspersor": {
        "padres": ["Lluvia"],  # Depende de Lluvia
        "cpt": {
            (True,): 0.01,
            (False,): 0.4
        }
    },
    "PastoMojado": {
        "padres": ["Lluvia", "Aspersor"],  # Depende de ambos
        "cpt": {
            (True, True): 0.99,
            (True, False): 0.8,
            (False, True): 0.9,
            (False, False): 0.0
        }
    }
}

# Orden topológico (padres primero)
orden = ["Lluvia", "Aspersor", "PastoMojado"]


# -----------------------------------------
# GENERAR TODAS LAS COMBINACIONES POSIBLES
# -----------------------------------------
def generar(vars):
    # Caso base: sin variables
    if not vars:
        return [{}]

    # Generamos combinaciones del resto
    resto = generar(vars[1:])
    resultado = []

    # Construimos nuevas combinaciones
    for r in resto:
        for valor in [True, False]:
            nuevo = r.copy()          # Copia de la asignación actual
            nuevo[vars[0]] = valor    # Asignamos valor a la variable
            resultado.append(nuevo)   # Guardamos combinación

    return resultado


# -----------------------------------------
# PROBABILIDAD CONJUNTA (REGLA DE LA CADENA)
# -----------------------------------------
def probabilidad_conjunta(asig):
    prob = 1.0  # Inicializamos probabilidad

    # Recorremos cada variable
    for var in orden:
        padres = red[var]["padres"]

        # Si no tiene padres
        if not padres:
            p = red[var]["cpt"][asig[var]]
        else:
            # Obtenemos valores de los padres
            vals = tuple(asig[p] for p in padres)

            # Probabilidad condicional
            p_true = red[var]["cpt"][vals]

            # Ajustamos si es True o False
            p = p_true if asig[var] else (1 - p_true)

        prob *= p  # Multiplicamos probabilidades

    return prob


# -----------------------------------------
# 🔥 INFERENCIA POR ENUMERACIÓN
# -----------------------------------------
def inferencia_enum(query, evidencia):

    total = 0.0       # Probabilidad total
    favorable = 0.0   # Casos donde query=True

    # Recorremos todos los posibles mundos
    for asig in generar(orden):

        # Verificamos si cumple la evidencia
        cumple = True
        for var in evidencia:
            if asig[var] != evidencia[var]:
                cumple = False
                break

        # Si no cumple, lo ignoramos
        if not cumple:
            continue

        # Calculamos probabilidad conjunta
        p = probabilidad_conjunta(asig)

        total += p  # Sumamos al total

        # Si además cumple el query
        if asig[query]:
            favorable += p

    # Evitamos división entre cero
    if total == 0:
        return 0

    # Probabilidad condicional final
    return favorable / total


# -----------------------------------------
# EJEMPLO DE USO (DENTRO DEL MISMO CÓDIGO)
# -----------------------------------------
# Queremos calcular:
# P(PastoMojado = True | Lluvia = True)

resultado = inferencia_enum(
    query="PastoMojado",
    evidencia={"Lluvia": True}
)

print("Resultado:", resultado)