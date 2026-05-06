# =========================================
# FUNCIÓN: MANTO DE MARKOV
# =========================================

def manto_markov(nodo, red):
    # Verificamos que el nodo exista en la red
    if nodo not in red:
        raise ValueError(f"El nodo '{nodo}' no existe en la red")

    # ================================
    # 1. OBTENER PADRES DEL NODO
    # ================================
    # Accedemos a la lista de padres directamente desde la red
    padres = red[nodo]["padres"]

    # ================================
    # 2. ENCONTRAR HIJOS DEL NODO
    # ================================
    # Inicializamos lista vacía para hijos
    hijos = []

    # Recorremos todos los nodos de la red
    for var in red:
        # Si el nodo actual aparece como padre de 'var'
        if nodo in red[var]["padres"]:
            # Entonces 'var' es hijo del nodo
            hijos.append(var)

    # ================================
    # 3. ENCONTRAR COPADRES (PADRES DE LOS HIJOS)
    # ================================
    # Lista para almacenar copadres
    copadres = []

    # Recorremos cada hijo encontrado
    for hijo in hijos:
        # Revisamos los padres de ese hijo
        for p in red[hijo]["padres"]:
            # Si el padre no es el nodo original
            # y no está ya en la lista
            if p != nodo and p not in copadres:
                copadres.append(p)

    # ================================
    # 4. UNIÓN DE TODOS LOS ELEMENTOS
    # ================================
    # El manto de Markov = padres + hijos + copadres
    manto = set(padres + hijos + copadres)

    # Retornamos el conjunto (sin duplicados)
    return manto    