"""
Realizar un programa que lea el contenido de un archivo y cambie las letras
minusculas a mayusculas y viceversa, imprimir resultado en consola
"""

file = open("mayus.txt", "r")
contenido = file.read()
guardando = []

for letra in contenido:
	if letra.isupper():
		minus = letra.lower()
		guardando.append(minus)
		
	if letra.islower():
		mayus = letra.upper()
		guardando.append(mayus)

	if(letra == " "): #para que respete el espacio en blanco
		guardando.append(" ")

texto = "".join(str(x) for x in guardando)
print(texto)
		

