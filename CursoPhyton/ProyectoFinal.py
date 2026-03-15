# Importa la función randrange del módulo random
# Esta función se utilizará para que la máquina elija un movimiento aleatorio
from random import randrange

# Se crea el tablero como una lista de listas (3x3)
# Cada número representa una casilla libre
# La máquina inicia colocando una 'X' en el centro
board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
]

# Función para mostrar el tablero en pantalla
def display_board(board):
    # Recorre cada fila del tablero
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        # Imprime el contenido de cada casilla de la fila
        print("|  {}  |  {}  |  {}  |".format(row[0], row[1], row[2]))
        print("|       |       |       |")
    print("+-------+-------+-------+")


# Función que permite al usuario ingresar su movimiento
def enter_move(board):
    while True:
        # Se pide al usuario que ingrese un número
        move = int(input("Ingresa tu movimiento: "))

        # Se valida que el número esté entre 1 y 9
        if move < 1 or move > 9:
            print("Movimiento inválido.")
            continue
        
        # Convierte el número ingresado en posición de fila y columna
        row = (move - 1) // 3
        col = (move - 1) % 3
        
        # Verifica que la casilla esté libre
        if board[row][col] not in ['X','O']:
            # Coloca la 'O' del jugador
            board[row][col] = 'O'
            break
        else:
            print("Ese cuadro ya está ocupado.")


# Función que devuelve las casillas libres del tablero
def free_fields(board):
    free = []

    # Recorre todas las posiciones del tablero
    for r in range(3):
        for c in range(3):
            # Si la casilla no tiene X ni O, está libre
            if board[r][c] not in ['X','O']:
                free.append((r,c))

    return free


# Función para verificar si un jugador ha ganado
def victory_for(board, sign):

    # Se revisan todas las combinaciones posibles para ganar
    if (board[0][0]==board[0][1]==board[0][2]==sign or
        board[1][0]==board[1][1]==board[1][2]==sign or
        board[2][0]==board[2][1]==board[2][2]==sign or
        board[0][0]==board[1][0]==board[2][0]==sign or
        board[0][1]==board[1][1]==board[2][1]==sign or
        board[0][2]==board[1][2]==board[2][2]==sign or
        board[0][0]==board[1][1]==board[2][2]==sign or
        board[0][2]==board[1][1]==board[2][0]==sign):

        return True
    
    return False


# Función que realiza el movimiento de la máquina
def draw_move(board):

    # Obtiene las casillas libres
    free = free_fields(board)

    # Si hay casillas libres
    if free:
        # Elige una posición aleatoria
        r = randrange(len(free))
        row, col = free[r]

        # Coloca una 'X'
        board[row][col] = 'X'


# Bucle principal del juego
while True:

    # Muestra el tablero
    display_board(board)

    # Turno del usuario
    enter_move(board)

    # Verifica si el jugador ganó
    if victory_for(board,'O'):
        display_board(board)
        print("¡Has ganado!")
        break

    # Si no hay casillas libres es empate
    if not free_fields(board):
        display_board(board)
        print("Empate.")
        break

    # Turno de la máquina
    draw_move(board)

    # Verifica si la máquina ganó
    if victory_for(board,'X'):
        display_board(board)
        print("La máquina ganó.")
        break

    # Si ya no hay casillas libres, es empate
    if not free_fields(board):
        display_board(board)
        print("Empate.")
        break