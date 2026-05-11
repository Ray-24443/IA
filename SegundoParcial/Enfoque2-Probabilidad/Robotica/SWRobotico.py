# ---------------------------------------------------------
# SOFTWARE ROBOTICO
# ---------------------------------------------------------

# Clase robot
class Robot:

    # Constructor
    def __init__(self):

        # Nombre del robot
        self.nombre = "Robot IA"

    # Método avanzar
    def avanzar(self):

        # Mostramos acción
        print("El robot avanza")

    # Método girar
    def girar(self):

        # Mostramos acción
        print("El robot gira")

# Creamos robot
robot = Robot()

# Ejecutamos acciones
robot.avanzar()

robot.girar()