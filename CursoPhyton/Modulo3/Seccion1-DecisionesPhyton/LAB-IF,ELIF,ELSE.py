year = int(input("Introduce un año: "))#el usuario ingresa un año

if year < 1582:#comparacion
	print("No esta dentro del período del calendario Gregoriano")
else:#si el año es mayor a 1582
	if year % 4 != 0:#si el año no es divisible entre 4
		print("Año Común")
	elif year % 100 != 0:#si el año no es divisible entre 100
		print("Año Bisiesto")
	elif year % 400 != 0:#si el año no es divisible entre 400
		print("Año Común")
	else:#de lo contrario
		print("Año Bisiesto")