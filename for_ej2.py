from string import ascii_uppercase

texto_usuario = input("Introduzca un texto:\n")

mayusculas = 0

for e in texto_usuario:
    #Espacios
    if e in ascii_uppercase:
        mayusculas += 1

print (f"Hay {mayusculas} mayusculas.\n")