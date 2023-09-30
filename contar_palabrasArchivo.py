"""
Contar cuantas palabras tiene un archivo de texto
mostrar el numero en consola
"""
file = open("prueba.txt", "r")
content = file.read()
words = len(content.split(" "))
print(words)

file.close()