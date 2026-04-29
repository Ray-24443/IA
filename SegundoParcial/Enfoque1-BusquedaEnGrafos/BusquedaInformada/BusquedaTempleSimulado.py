# ================== TEMPLE SIMULADO ==================

import random  # Librería para aleatoriedad
import math    # Librería para funciones matemáticas

# Definición del grafo
grafo = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'D': 4, 'E': 1},
    'C': {'A': 5, 'F': 3},
    'D': {'B': 4},
    'E': {'B': 1, 'F': 2},
    'F': {'C': 3, 'E': 2}
}

# Definición de heurística
heuristica = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 0
}

# Función principal
def simulated_annealing(inicio, temp=100, enfriamiento=0.9):
    
    actual = inicio  # Nodo actual
    camino = [actual]  # Registro del camino
    
    # Mientras la temperatura sea mayor que 1
    while temp > 1:
        
        vecinos = list(grafo[actual].keys())  # Obtener vecinos
        siguiente = random.choice(vecinos)  # Elegir vecino aleatorio
        
        # Calcular diferencia de heurística
        delta = heuristica[siguiente] - heuristica[actual]
        
        # Si mejora o se acepta probabilísticamente
        if delta < 0 or random.random() < math.exp(-delta / temp):
            
            actual = siguiente  # Moverse al vecino
            camino.append(actual)  # Guardar camino
        
        temp *= enfriamiento  # Reducir temperatura
    
    return camino  # Retornar camino

# Ejecutar
resultado = simulated_annealing('A')

# Mostrar resultado
print("Camino encontrado:", resultado)