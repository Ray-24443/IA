import random  # Aleatoriedad

# Definimos el grafo
grafo = {
    'A': ['B', 'C'],  # Decisiones
    'B': ['D'],       # Camino a meta
    'C': ['D'],
    'D': []
}

# Imprimir grafo
print("Grafo:", grafo)

# Recompensas
rewards = {'A': 0, 'B': 0, 'C': 0, 'D': 10}

# Inicializamos tabla Q
Q = {}  # Diccionario vacío

# Inicializamos valores en 0
for estado in grafo:  # Para cada estado
    for accion in grafo[estado]:  # Para cada acción posible
        Q[(estado, accion)] = 0  # Inicializar en 0

alpha = 0.1  # Aprendizaje
gamma = 0.9  # Descuento
epsilon = 0.2  # Exploración

# Entrenamiento
for episodio in range(100):  # Episodios
    estado = 'A'  # Inicial
    
    while estado != 'D':  # Hasta llegar a meta
        if random.random() < epsilon:  # Explorar
            accion = random.choice(grafo[estado])  # Aleatorio
        else:
            accion = max(grafo[estado], key=lambda a: Q[(estado, a)])  # Mejor acción
        
        siguiente = accion  # Transición
        
        if grafo[siguiente]:  # Si no es terminal
            max_q = max(Q[(siguiente, a)] for a in grafo[siguiente])  # Mejor Q futuro
        else:
            max_q = 0  # Terminal
        
        Q[(estado, accion)] = Q[(estado, accion)] + alpha * (rewards[siguiente] + gamma * max_q - Q[(estado, accion)])  # Update
        
        estado = siguiente  # Avanzar

# Resultado
print("Tabla Q:", Q)