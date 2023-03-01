from os import system as s
from string import ascii_letters

s("cls")
print("Programa para saber el mayor y el menor de los numeros que el usuario digita!!!")

numeros = []
eleccion = None

while eleccion not in ["q", "Q"]:
    eleccion = input("Digite un numero que quiera añadir a la lista('Q' para terminar de añadir):\n")
    if eleccion in ["q", "Q"]:
        if not numeros:
            s("cls")
            print("La lista esta vacia\n")
        else:
            s("cls")
            print(f"El numero mas pequeño es {min(numeros)} y el mas grande es {max(numeros)}\n")
    elif eleccion in ascii_letters and eleccion not in ["q", "Q"]:
        s("cls")
        print("Favor de digitar solo numeros\n")
    else:
        numeros.append(int(eleccion))
        s("cls")
