import re

anoActual = 2023

nombre = input("¿Cuál es tu nombre(s)? ")
primerApellido = input("¿Cuál es tu primer apellido? ")
segundoApellido = input("¿Cuál es tu segundo apellido? ")
anoNacimiento = input("¿En qué año naciste? ")
fechaNacimiento = input("¿En qué mes y día naciste? (en el siguiente formato “mm-dd”) ")

nombreCompleto = nombre + " " + primerApellido + " " + segundoApellido

print("Este es tu nombre completo en mayúsculas " + nombreCompleto.upper() + ".")
print("Este es tu nombre completo en minúsculas " + nombreCompleto.lower() + ".")
print("Esta es tu fecha de nacimiento " + fechaNacimiento + "-" + anoNacimiento)
edad = anoActual - int(anoNacimiento)
print("Esta es tu edad "  + str(edad) + ".")
vocales = re.findall('[aeiouAEIOU]', nombreCompleto)
numeroVocales = len(vocales)
print( "Tu nombre completo tiene " + str(numeroVocales) + " vocales.")
numeroLetras = len(re.findall('[a-zA-Z]', nombreCompleto))
print("Tu nombre completo tiene " + str(numeroLetras) + " letras.")
print("¿Tu edad es un carácter de tipo número? " + str(type(edad) == int))
nombreSinEspacios = nombreCompleto.replace(" ","")
print("¿Tu nombre completo es un carácter de tipo alfanumérico? " + str(nombreSinEspacios.isalpha()) )
print("Tu edad en 10 años será " + str(edad + 10) )
media = (edad + (edad + 20))/2
print("La media de tu edad actual y tu edad en 20 años es " + str(media))
