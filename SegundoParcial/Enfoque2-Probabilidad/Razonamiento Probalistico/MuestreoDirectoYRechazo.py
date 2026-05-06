# =========================================
# MUESTREO DIRECTO Y POR RECHAZO
# =========================================

import random

# Red igual
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

orden = ["Lluvia", "Aspersor", "PastoMojado"]


# Muestreo directo
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


# Muestreo por rechazo
def rechazo(query, evidencia, N=1000):
    aceptadas = 0
    favor = 0

    for _ in range(N):
        m = muestreo_directo()

        if all(m[e] == evidencia[e] for e in evidencia):
            aceptadas += 1
            if m[query]:
                favor += 1

    return favor / aceptadas if aceptadas > 0 else 0


# EJEMPLO
print("Rechazo:", rechazo("PastoMojado", {"Lluvia": True}))