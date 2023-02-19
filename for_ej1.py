texto_usuario = input("Introduzca un texto:\n")

espacio_c = 0
punto_c = 0
coma_c = 0


for e in texto_usuario:
    #Espacios
    if e == " ":
        espacio_c += 1
    #Puntos
    elif e == ".":
        punto_c += 1
    #Comas
    elif e == ",":
        coma_c += 1

print (f"Hay {espacio_c} espacios, {punto_c} puntos y {coma_c} comas.\n")