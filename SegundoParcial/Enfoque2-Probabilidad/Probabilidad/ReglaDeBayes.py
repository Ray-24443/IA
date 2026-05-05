# Definimos probabilidades

P_A = 0.01  # Probabilidad de enfermedad (1%)
P_B_dado_A = 0.9  # Probabilidad de positivo si está enfermo

P_B_dado_no_A = 0.05  # Probabilidad de falso positivo

# Calculamos P(B)
P_B = (P_B_dado_A * P_A) + (P_B_dado_no_A * (1 - P_A))  # Ley total

# Aplicamos Bayes
P_A_dado_B = (P_B_dado_A * P_A) / P_B  # Fórmula

# Resultado
print("P(Enfermo | Positivo):", P_A_dado_B)