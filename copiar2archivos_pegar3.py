"""
Esscribe un programa que lea 2 archivos y guarde el contenido
de ambis en un tercer archivo
"""
file_one = open("uno.txt", "r")
file_two = open("dos.txt", "r")

f_one = file_one.read()
f_two = file_two.read()

file_three = open("resultado.txt", "a")
file_three.write(f_one)
file_three.write(f_two)

file_one.close()
file_two.close()
file_three.close()