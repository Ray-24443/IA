# ================================
# ITERACION DE POLITICAS
# ================================

# Grafo de estados
grafo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

# Recompensas
recompensa = {
    'A': 1,
    'B': 5,
    'C': 2,
    'D': 10
}

# Política inicial (elige primer vecino)
politica = {nodo: (grafo[nodo][0] if grafo[nodo] else None) for nodo in grafo}

# Valores iniciales
V = {nodo: 0 for nodo in grafo}

gamma = 0.9  # Factor de descuento

# Evaluación de política
def evaluar():
    for _ in range(10):  # Iteraciones
        for nodo in grafo:  # Recorremos nodos
            if politica[nodo] is None:  # Estado terminal
                continue  # Saltamos
            vecino = politica[nodo]  # Acción actual
            V[nodo] = recompensa[vecino] + gamma * V[vecino]  # Actualizamos

# Mejora de política
def mejorar():
    estable = True  # Bandera de estabilidad

    for nodo in grafo:  # Recorremos nodos
        if not grafo[nodo]:  # Terminal
            continue

        mejor = None  # Mejor acción
        mejor_valor = float('-inf')  # Inicializamos

        for vecino in grafo[nodo]:  # Probamos acciones
            valor = recompensa[vecino] + gamma * V[vecino]  # Evaluamos
            if valor > mejor_valor:  # Si mejora
                mejor_valor = valor
                mejor = vecino

        if politica[nodo] != mejor:  # Si cambia
            politica[nodo] = mejor
            estable = False  # No es estable

    return estable  # Regresamos estabilidad

# Iteramos hasta converger
while True:
    evaluar()  # Evaluamos política
    if mejorar():  # Mejoramos
        break  # Si ya es óptima, salimos

# Resultado
print("Politica optima:", politica)