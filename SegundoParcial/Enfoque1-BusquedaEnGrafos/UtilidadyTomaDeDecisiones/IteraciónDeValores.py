# ================================
# ITERACION DE VALORES
# ================================

# Grafo de estados
grafo = {
    'A': ['B', 'C'],  # Desde A puedes ir a B o C
    'B': ['D'],       # Desde B a D
    'C': ['D'],       # Desde C a D
    'D': []           # Estado terminal
}

# Recompensas por estado
recompensa = {
    'A': 1,
    'B': 5,
    'C': 2,
    'D': 10
}

# Factor de descuento
gamma = 0.9  # Importancia del futuro

# Inicializamos valores en 0
V = {nodo: 0 for nodo in grafo}  # Diccionario de valores

# Iteramos varias veces
for i in range(10):  # Número de iteraciones
    nuevo_V = V.copy()  # Copiamos valores actuales

    for nodo in grafo:  # Recorremos cada nodo
        if not grafo[nodo]:  # Si no tiene vecinos (terminal)
            continue  # Saltamos

        valores = []  # Lista de posibles valores

        for vecino in grafo[nodo]:  # Revisamos transiciones
            valor = recompensa[vecino] + gamma * V[vecino]  # Bellman
            valores.append(valor)  # Guardamos

        nuevo_V[nodo] = max(valores)  # Elegimos mejor acción

    V = nuevo_V  # Actualizamos valores

# Mostramos resultados
print("Valores finales:", V)