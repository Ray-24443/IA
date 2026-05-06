# =========================================
# REGLA DE LA CADENA
# =========================================

def probabilidad_conjunta(asignacion, red, orden):
    prob = 1.0  # Inicializamos la probabilidad total

    for var in orden:  # Recorremos en orden topológico
        padres = red[var]["padres"]  # Obtenemos padres

        # Caso 1: Nodo sin padres
        if not padres:
            # Accedemos directamente a la probabilidad
            if asignacion[var] not in red[var]["cpt"]:
                raise ValueError(f"Valor inválido en {var}")
            p = red[var]["cpt"][asignacion[var]]

        # Caso 2: Nodo con padres
        else:
            # Construimos la tupla de valores de los padres
            try:
                valores_padres = tuple(asignacion[p] for p in padres)
            except KeyError:
                raise ValueError(f"Falta asignación de algún padre de {var}")

            # Verificamos que exista en la CPT
            if valores_padres not in red[var]["cpt"]:
                raise ValueError(f"No existe combinación {valores_padres} en {var}")

            p_true = red[var]["cpt"][valores_padres]

            # Si la variable es True usamos p, si es False usamos complemento
            p = p_true if asignacion[var] else (1 - p_true)

        prob *= p  # Multiplicamos

    return prob