# ================================
# FUNCION DE UTILIDAD
# ================================

# Definimos el grafo como un diccionario
# Cada nodo representa un estado
# Cada arista representa transición posible
grafo = {
    'A': ['B', 'C'],   # Desde A puedes ir a B o C
    'B': ['D'],        # Desde B puedes ir a D
    'C': ['D'],        # Desde C puedes ir a D
    'D': []            # D es estado final
}

# Definimos utilidad de cada estado
utilidad = {
    'A': 10,   # Utilidad baja
    'B': 50,   # Mejor estado
    'C': 30,   # Estado intermedio
    'D': 100   # Estado objetivo
}

# Función para obtener utilidad de un nodo
def obtener_utilidad(nodo):
    return utilidad[nodo]  # Regresa valor de utilidad del nodo

# Recorremos el grafo mostrando utilidades
for nodo in grafo:  # Iteramos sobre cada nodo
    print("Nodo:", nodo, "-> Utilidad:", obtener_utilidad(nodo))  # Imprimimos