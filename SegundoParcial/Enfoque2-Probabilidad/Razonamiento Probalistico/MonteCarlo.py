# =========================================
# MCMC (GIBBS SAMPLING) - COMPLETO
# =========================================

import random  # Necesario para generar números aleatorios


# -----------------------------------------
# RED BAYESIANA (EJEMPLO)
# -----------------------------------------
red = {
    "Lluvia": {"padres": [], "cpt": {True: 0.2, False: 0.8}},
    "Aspersor": {"padres": ["Lluvia"], "cpt": {(True,): 0.01, (False,): 0.4}},
    "PastoMojado": {
        "padres": ["Lluvia", "Aspersor"],
        "cpt": {
            (True, True): 0.99,
            (True, False): 0.8,
            (False, True): 0.9,
            (False, False): 0.0
        }
    }
}

# Orden correcto (padres primero)
orden = ["Lluvia", "Aspersor", "PastoMojado"]


# -----------------------------------------
# MUESTREO DIRECTO (NECESARIO PARA INICIALIZAR)
# -----------------------------------------
def muestreo_directo():
    muestra = {}

    for var in orden:
        padres = red[var]["padres"]

        if not padres:
            p = red[var]["cpt"][True]
        else:
            vals = tuple(muestra[p] for p in padres)
            p = red[var]["cpt"][vals]

        muestra[var] = random.random() < p

    return muestra


# -----------------------------------------
# PROBABILIDAD LOCAL
# -----------------------------------------
def prob_local(var, estado):
    padres = red[var]["padres"]

    if not padres:
        return red[var]["cpt"][True]

    vals = tuple(estado[p] for p in padres)
    return red[var]["cpt"][vals]


# -----------------------------------------
# GIBBS SAMPLING (MCMC)
# -----------------------------------------
def gibbs(query, evidencia, pasos=2000):

    # Estado inicial aleatorio
    estado = muestreo_directo()

    # Fijar evidencia
    for e in evidencia:
        estado[e] = evidencia[e]

    conteo = 0

    # Variables que sí se pueden cambiar
    no_evidencia = [v for v in orden if v not in evidencia]

    # Iteraciones
    for _ in range(pasos):

        for var in no_evidencia:

            # Probabilidad de True
            estado[var] = True
            p_true = prob_local(var, estado)

            # Probabilidad de False
            estado[var] = False
            p_false = prob_local(var, estado)

            # Normalización
            prob = p_true / (p_true + p_false)

            # Muestreo
            estado[var] = random.random() < prob

        # Contamos si cumple query
        if estado[query]:
            conteo += 1

    return conteo / pasos


# -----------------------------------------
# EJEMPLO
# -----------------------------------------
print("Resultado Gibbs:", gibbs("PastoMojado", {"Lluvia": True}))