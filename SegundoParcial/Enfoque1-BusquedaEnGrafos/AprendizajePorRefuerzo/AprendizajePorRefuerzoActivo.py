import random  # Para decisiones aleatorias

# Definimos el grafo
grafo = {
    'A': ['B', 'C'],  # Opciones desde A
    'B': ['D'],       # B lleva a D
    'C': ['D'],       # C lleva a D
    'D': []           # Final
}

# Imprimir grafo
print("Grafo:", grafo)

# Recompensas
rewards = {'A': 0, 'B': 0, 'C': 0, 'D': 10}

# Valores iniciales
V = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

gamma = 0.9  # Descuento
alpha = 0.1  # Aprendizaje

# Entrenamiento
for episodio in range(100):  # 100 episodios
    estado = 'A'  # Inicio
    
    while estado != 'D':  # Hasta meta
        siguiente = random.choice(grafo[estado])  # Elegir aleatorio
        
        V[estado] = V[estado] + alpha * (rewards[estado] + gamma * V[siguiente] - V[estado])  # Actualizar
        
        estado = siguiente  # Avanzar

# Resultado
print("Valores aprendidos:", V)