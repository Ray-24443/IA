# =========================================
# ELIMINACIÓN DE VARIABLES
# =========================================

# Red Bayesiana de ejemplo
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


# Generar combinaciones
def generar(vars):
    if not vars:
        return [{}]
    resto = generar(vars[1:])
    resultado = []
    for r in resto:
        for v in [True, False]:
            nuevo = r.copy()
            nuevo[vars[0]] = v
            resultado.append(nuevo)
    return resultado


# Crear factor
def crear_factor(var):
    padres = red[var]["padres"]
    tabla = {}

    for asig in generar([var] + padres):
        key = tuple(asig[v] for v in [var] + padres)

        if not padres:
            p = red[var]["cpt"][asig[var]]
        else:
            vals = tuple(asig[p] for p in padres)
            p_true = red[var]["cpt"][vals]
            p = p_true if asig[var] else (1 - p_true)

        tabla[key] = p

    return {"vars": [var] + padres, "tabla": tabla}


# Multiplicar factores
def multiplicar(f1, f2):
    vars_nuevas = list(set(f1["vars"] + f2["vars"]))
    tabla = {}

    for asig in generar(vars_nuevas):
        key = tuple(asig[v] for v in vars_nuevas)
        k1 = tuple(asig[v] for v in f1["vars"])
        k2 = tuple(asig[v] for v in f2["vars"])
        tabla[key] = f1["tabla"][k1] * f2["tabla"][k2]

    return {"vars": vars_nuevas, "tabla": tabla}


# Marginalizar variable
def marginalizar(factor, var):
    nuevas_vars = [v for v in factor["vars"] if v != var]
    tabla = {}

    for asig in generar(nuevas_vars):
        total = 0
        for val in [True, False]:
            ext = asig.copy()
            ext[var] = val
            key = tuple(ext[v] for v in factor["vars"])
            total += factor["tabla"][key]

        tabla[tuple(asig[v] for v in nuevas_vars)] = total

    return {"vars": nuevas_vars, "tabla": tabla}


# Eliminación de variables
def eliminacion(query, evidencia):
    factores = [crear_factor(v) for v in orden]

    ocultas = [v for v in orden if v != query and v not in evidencia]

    for var in ocultas:
        relacionados = [f for f in factores if var in f["vars"]]

        nuevo = relacionados[0]
        for f in relacionados[1:]:
            nuevo = multiplicar(nuevo, f)

        nuevo = marginalizar(nuevo, var)

        factores = [f for f in factores if f not in relacionados]
        factores.append(nuevo)

    resultado = factores[0]
    for f in factores[1:]:
        resultado = multiplicar(resultado, f)

    total = sum(resultado["tabla"].values())
    favor = 0

    for k, v in resultado["tabla"].items():
        if k[resultado["vars"].index(query)]:
            favor += v

    return favor / total


# EJEMPLO
print("Eliminación:", eliminacion("PastoMojado", {"Lluvia": True}))