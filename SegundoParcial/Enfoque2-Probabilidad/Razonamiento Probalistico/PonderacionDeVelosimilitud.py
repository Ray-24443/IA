# =========================================
# PONDERACIÓN DE VEROSIMILITUD (COMPLETO)
# =========================================

import random  # IMPORTANTE: sin esto falla random.random()

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

# Orden topológico
orden = ["Lluvia", "Aspersor", "PastoMojado"]


# =========================================
# PONDERACIÓN DE VEROSIMILITUD
# =========================================
def ponderacion(query, evidencia, N=1000):

    total = 0.0   # Suma total de pesos
    favor = 0.0   # Suma de pesos donde query=True

    # Generamos N muestras
    for _ in range(N):

        muestra = {}  # Diccionario para la muestra actual
        peso = 1.0    # Peso de la muestra

        # Recorremos variables en orden correcto
        for var in orden:

            padres = red[var]["padres"]  # Obtenemos padres

            # Si no tiene padres
            if not padres:
                p = red[var]["cpt"][True]
            else:
                # Obtenemos valores de padres ya muestreados
                vals = tuple(muestra[p] for p in padres)
                p = red[var]["cpt"][vals]

            # Si la variable está en la evidencia
            if var in evidencia:
                # Ajustamos el peso
                if evidencia[var]:
                    peso *= p
                else:
                    peso *= (1 - p)

                # Fijamos el valor (no se muestrea)
                muestra[var] = evidencia[var]

            else:
                # Muestreamos normalmente
                muestra[var] = random.random() < p

        # Acumulamos pesos
        total += peso

        # Si cumple el query
        if muestra[query]:
            favor += peso

    # Evitar división entre cero
    if total == 0:
        return 0

    return favor / total


# -----------------------------------------
# EJEMPLO
# -----------------------------------------
print("Resultado:", ponderacion("PastoMojado", {"Lluvia": True}))