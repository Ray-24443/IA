# ================================
# DEFINICIÓN DE LA RED BAYESIANA
# ================================

# Orden topológico (IMPORTANTE para muestreo)
orden = ["Lluvia", "Aspersor", "PastoMojado"]

# Definición de la red
red = {
    "Lluvia": {
        "padres": [],
        "cpt": {True: 0.2, False: 0.8}
    },
    "Aspersor": {
        "padres": ["Lluvia"],
        "cpt": {
            (True,): 0.01,
            (False,): 0.4
        }
    },
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

# Grafo dirigido (para visualización conceptual)
grafo = {
    "Lluvia": ["Aspersor", "PastoMojado"],
    "Aspersor": ["PastoMojado"],
    "PastoMojado": []
}