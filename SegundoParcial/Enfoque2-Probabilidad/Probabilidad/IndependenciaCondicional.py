# Ejemplo:
# A = Lluvia
# B = Tráfico
# C = Día de la semana

# Probabilidades dadas C (fin de semana)
P_A_dado_C = 0.2  # P(Lluvia | fin de semana)
P_B_dado_C = 0.3  # P(Tráfico | fin de semana)

# Probabilidad conjunta si son independientes
P_AyB_dado_C = P_A_dado_C * P_B_dado_C  # Multiplicación

# Mostramos resultados
print("P(A y B | C):", P_AyB_dado_C)

# Verificamos independencia
print("Si A y B son independientes dado C, se cumple:")
print("P(A y B | C) = P(A|C) * P(B|C)")