# ================== ALGORITMO GENÉTICO ==================

import random  # Librería para generar valores aleatorios

# Definición del grafo
grafo = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'D': 4, 'E': 1},
    'C': {'A': 5, 'F': 3},
    'D': {'B': 4},
    'E': {'B': 1, 'F': 2},
    'F': {'C': 3, 'E': 2}
}

# Heurística (menor es mejor)
heuristica = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 0
}

# Función de fitness (calidad de solución)
def fitness(nodo):
    return -heuristica[nodo]  # Negativo porque menor heurística es mejor

# Función principal del algoritmo genético
def algoritmo_genetico(poblacion_size=4, generaciones=10):
    
    # Crear población inicial aleatoria
    poblacion = [random.choice(list(grafo.keys())) for _ in range(poblacion_size)]
    
    # Iterar generaciones
    for g in range(generaciones):
        
        # Evaluar fitness de cada individuo
        poblacion = sorted(poblacion, key=lambda x: fitness(x), reverse=True)
        
        nueva_poblacion = poblacion[:2]  # Seleccionar los mejores (elitismo)
        
        # Generar nuevos individuos
        while len(nueva_poblacion) < poblacion_size:
            
            # Seleccionar padres aleatoriamente
            padre1 = random.choice(poblacion[:2])
            padre2 = random.choice(poblacion[:2])
            
            # Cruce: elegir uno de los dos padres
            hijo = random.choice([padre1, padre2])
            
            # Mutación: cambiar a un vecino aleatorio
            if random.random() < 0.3:
                hijo = random.choice(list(grafo[hijo].keys()))
            
            nueva_poblacion.append(hijo)
        
        poblacion = nueva_poblacion  # Actualizar población
    
    # Retornar mejor individuo
    mejor = max(poblacion, key=lambda x: fitness(x))
    
    return mejor

# Ejecutar algoritmo
resultado = algoritmo_genetico()

# Mostrar resultado
print("Mejor nodo encontrado:", resultado)  