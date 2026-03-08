# función que convierte litros/100km a millas por galón
def liters_100km_to_miles_gallon(liters):

    miles = 100 / 1.609344
    gallons = liters / 3.785411784

    return miles / gallons


# función que convierte millas por galón a litros/100km
def miles_gallon_to_liters_100km(miles):

    km = miles * 1.609344
    liters = 3.785411784

    return liters / (km / 100)


# pruebas
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10))

print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))