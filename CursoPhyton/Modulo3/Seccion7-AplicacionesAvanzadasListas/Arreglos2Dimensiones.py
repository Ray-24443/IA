# Crea un tablero de ajedrez de 8x8 lleno con la palabra 'EMPTY'
# La comprensión de listas genera 8 listas (filas) y cada una contiene 8 elementos
board = [['EMPTY' for i in range(8)] for j in range(8)]
# Coloca una torre (ROOK) en la esquina superior izquierda del tablero
board[0][0] = 'ROOK'
# Coloca una torre (ROOK) en la esquina superior derecha del tablero
board[0][7] = 'ROOK'
# Coloca una torre (ROOK) en la esquina inferior izquierda del tablero
board[7][0] = 'ROOK'
# Coloca una torre (ROOK) en la esquina inferior derecha del tablero
board[7][7] = 'ROOK'
# Coloca un caballo (KNIGHT) en la fila 4 columna 2 del tablero
board[4][2] = 'KNIGHT'
# Coloca un peón (PAWN) en la fila 3 columna 4 del tablero
board[3][4] = 'PAWN'
# Imprime todo el tablero en forma de lista de listas
print(board)