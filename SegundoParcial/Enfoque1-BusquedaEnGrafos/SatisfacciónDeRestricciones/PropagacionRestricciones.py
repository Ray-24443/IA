# ================== Propagacion Restricciones ==================

from collections import deque  # Importar estructura de cola

# Variables
variables = ['A', 'B', 'C', 'D']

# Dominios
dominios = {
    'A': ['Rojo', 'Verde', 'Azul'],
    'B': ['Rojo', 'Verde', 'Azul'],
    'C': ['Rojo', 'Verde', 'Azul'],
    'D': ['Rojo', 'Verde', 'Azul']
}

# Restricciones
vecinos = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Función revisar consistencia
def revisar(xi, xj):
    
    revisado = False  # Bandera de cambio
    
    for x in dominios[xi][:]:
        
        # Si todos los valores de xj son iguales a x
        if all(x == y for y in dominios[xj]):
            
            dominios[xi].remove(x)  # Eliminar valor inconsistente
            revisado = True
    
    return revisado

# Algoritmo AC-3
def ac3():
    
    cola = deque([(xi, xj) for xi in variables for xj in vecinos[xi]])
    
    while cola:
        
        xi, xj = cola.popleft()
        
        if revisar(xi, xj):
            
            if not dominios[xi]:
                return False
            
            for xk in vecinos[xi]:
                if xk != xj:
                    cola.append((xk, xi))
    
    return True

# Ejecutar
print("AC-3:", ac3())
print("Dominios:", dominios)