def imc(peso,altura): #defino la funcion
    if altura<1.0 or altura>2.5 or peso<20 or peso>200: #comparo si el peso o la altura es un dato invalido
        return None #retorna None
    
    return peso/altura**2 #retorna la operacion para calcular IMC


print(imc(52.5, 1.65)) #calculo el IMC con los parametros ingresados
