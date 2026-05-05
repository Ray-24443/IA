# Definimos el grafo como diccionario (lista de adyacencia)
grafo = {
    'A': ['B', 'C'],  # Desde A se puede ir a B o C
    'B': ['D'],       # Desde B se va a D
    'C': ['D'],       # Desde C se va a D
    'D': []           # D es estado final
}

# Imprimimos el grafo
print("Grafo:")
for nodo in grafo:  # Recorremos cada nodo
    print(nodo, "->", grafo[nodo])  # Mostramos conexiones

# Definimos recompensas por estado
rewards = {'A': 0, 'B': 0, 'C': 0, 'D': 10}  # Solo D tiene recompensa

# Definimos política fija
policy = {'A': 'B', 'B': 'D', 'C': 'D'}  # No cambia

# Inicializamos valores de estados
V = {'A': 0, 'B': 0, 'C': 0, 'D': 0}  # Todos en 0

gamma = 0.9  # Factor de descuento

# Iteramos para calcular valores
for i in range(10):  # 10 iteraciones
    for estado in V:  # Recorremos estados
        if estado in policy:  # Si tiene acción definida
            siguiente = policy[estado]  # Obtener siguiente estado
            V[estado] = rewards[estado] + gamma * V[siguiente]  # Bellman

# Mostramos resultado
print("Valores finales:", V)