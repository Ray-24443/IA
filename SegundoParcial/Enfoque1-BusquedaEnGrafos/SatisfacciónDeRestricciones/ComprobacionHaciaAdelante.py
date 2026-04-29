# ================== FORWARD CHECKING ==================

# Definir variables
variables = ['A', 'B', 'C', 'D']

# Definir dominios
dominios = {
    'A': ['Rojo', 'Verde', 'Azul'],
    'B': ['Rojo', 'Verde', 'Azul'],
    'C': ['Rojo', 'Verde', 'Azul'],
    'D': ['Rojo', 'Verde', 'Azul']
}

# Definir restricciones
vecinos = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Verificar consistencia
def es_valido(variable, valor, asignacion):
    
    for vecino in vecinos[variable]:
        
        if vecino in asignacion:
            
            if asignacion[vecino] == valor:
                return False
    
    return True

# Función Forward Checking
def forward_checking(asignacion={}, dominios_local=None):
    
    # Inicializar copia de dominios
    if dominios_local is None:
        dominios_local = {v: list(dominios[v]) for v in variables}
    
    # Si solución completa
    if len(asignacion) == len(variables):
        return asignacion
    
    # Seleccionar variable
    for variable in variables:
        if variable not in asignacion:
            break
    
    # Probar valores
    for valor in dominios_local[variable]:
        
        if es_valido(variable, valor, asignacion):
            
            nueva_asignacion = asignacion.copy()
            nueva_asignacion[variable] = valor
            
            nuevos_dominios = {v: list(dominios_local[v]) for v in variables}
            
            # Eliminar valores conflictivos
            for vecino in vecinos[variable]:
                if valor in nuevos_dominios[vecino]:
                    nuevos_dominios[vecino].remove(valor)
            
            resultado = forward_checking(nueva_asignacion, nuevos_dominios)
            
            if resultado:
                return resultado
    
    return None

# Ejecutar
print("Forward Checking:", forward_checking())