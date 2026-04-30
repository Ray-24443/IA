# ================================
# SALTO ATRÁS DIRIGIDO POR CONFLICTOS
# ================================

# Definimos el grafo como un problema de coloreo
# Cada nodo es una variable y las aristas representan restricciones
grafo = {
    'A': ['B', 'C'],   # A no puede tener el mismo color que B ni C
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Dominio de colores posibles
colores = ['Rojo', 'Verde', 'Azul']

# Diccionario donde guardamos la asignación actual
asignacion = {}

# Diccionario para registrar conflictos
conflictos = {var: set() for var in grafo}

# Función que verifica si una asignación es válida
def es_valido(variable, valor):
    for vecino in grafo[variable]:  # Revisamos vecinos
        if vecino in asignacion and asignacion[vecino] == valor:
            return False  # Conflicto: mismo color
    return True

# Función principal de backjumping
def backjumping(variables):
    if len(asignacion) == len(variables):
        return True  # Solución completa

    # Seleccionamos la siguiente variable
    variable = variables[len(asignacion)]

    for valor in colores:  # Probamos cada color
        if es_valido(variable, valor):
            asignacion[variable] = valor  # Asignamos

            if backjumping(variables):  # Llamada recursiva
                return True

            # Si falla, eliminamos asignación
            del asignacion[variable]
        else:
            # Registramos conflicto
            for vecino in grafo[variable]:
                if vecino in asignacion:
                    conflictos[variable].add(vecino)

    return False  # No hay solución

# Lista de variables
variables = list(grafo.keys())

# Ejecutamos
if backjumping(variables):
    print("Solución encontrada:", asignacion)
else:
    print("No hay solución")