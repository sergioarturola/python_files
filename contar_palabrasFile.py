file = open("Archivo1.txt", "r")
num_caracteres = file.read()
#para quitar los espacios en blanco
letras = num_caracteres.split()
#para obtener el numero total
numero_palabras = len(letras)

print("El numero de palabras del archivo es: ", numero_palabras)
