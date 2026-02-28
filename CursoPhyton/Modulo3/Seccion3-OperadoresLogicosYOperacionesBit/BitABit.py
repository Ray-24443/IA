# Asignación de valores iniciales
x = 4   # Número entero 4  -> binario: 0100
y = 1   # Número entero 1  -> binario: 0001

# Operador AND bit a bit (&)
# Compara cada bit y devuelve 1 solo si ambos bits son 1
# 0100 & 0001 = 0000 -> 0
a = x & y

# Operador OR bit a bit (|)
# Devuelve 1 si al menos uno de los bits es 1
# 0100 | 0001 = 0101 -> 5
b = x | y

# Operador NOT bit a bit (~)
# Invierte todos los bits (complemento a 2 en Python)
# Regla: ~n = -(n + 1)
# ~4 = -5
c = ~x  # ¡difícil!

# Operador XOR bit a bit (^)
# Devuelve 1 si los bits son diferentes
# 0100 ^ 0101 = 0001 -> 1
d = x ^ 5

# Desplazamiento a la derecha (>>)
# Mueve los bits 2 posiciones a la derecha
# 0100 >> 2 = 0001 -> 1
e = x >> 2

# Desplazamiento a la izquierda (<<)
# Mueve los bits 2 posiciones a la izquierda
# 0100 << 2 = 10000 -> 16
f = x << 2

# Imprime los resultados de todas las operaciones
print(a, b, c, d, e, f)