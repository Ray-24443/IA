# Definimos el grafo
grafo = {
    'A': ['B', 'C'],  # Decisiones
    'B': ['D'],       # Camino
    'C': ['D'],
    'D': []
}

# Imprimir grafo
print("Grafo:", grafo)

# Recompensas
rewards = {'A': 0, 'B': 0, 'C': 0, 'D': 10}

# Política inicial
policy = {'A': 'B', 'B': 'D', 'C': 'D'}

# Valores iniciales
V = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

gamma = 0.9  # Descuento

# Iteración de política
for i in range(10):  # Iteraciones
    
    # Evaluación
    for estado in policy:  # Estados con política
        siguiente = policy[estado]  # Siguiente estado
        V[estado] = rewards[estado] + gamma * V[siguiente]  # Bellman
    
    # Mejora
    for estado in grafo:  # Recorrer estados
        if grafo[estado]:  # Si tiene acciones
            mejor_accion = None  # Inicial
            mejor_valor = -9999  # Muy bajo
            
            for accion in grafo[estado]:  # Probar acciones
                valor = rewards[estado] + gamma * V[accion]  # Evaluar
                
                if valor > mejor_valor:  # Comparar
                    mejor_valor = valor  # Actualizar
                    mejor_accion = accion  # Guardar
            
            policy[estado] = mejor_accion  # Actualizar política

# Resultado
print("Política óptima:", policy)
print("Valores:", V)