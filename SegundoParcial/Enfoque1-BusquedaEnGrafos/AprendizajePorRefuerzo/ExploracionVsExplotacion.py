import random  # Aleatorio

# Grafo simple
grafo = {
    'A': ['B', 'C']  # Dos opciones
}

# Imprimir grafo
print("Grafo:", grafo)

# Recompensas
rewards = {'B': 10, 'C': 5}

# Valores iniciales
Q = {'B': 0, 'C': 0}

epsilon = 0.3  # Probabilidad de explorar
alpha = 0.1  # Aprendizaje

# Simulación
for i in range(100):  # Iteraciones
    if random.random() < epsilon:  # Explorar
        accion = random.choice(grafo['A'])  # Elegir aleatorio
    else:
        accion = max(Q, key=Q.get)  # Mejor opción
    
    Q[accion] = Q[accion] + alpha * (rewards[accion] - Q[accion])  # Actualizar

# Resultado
print("Valores finales:", Q)