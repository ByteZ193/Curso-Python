from os import system

system("cls")
print("Progama lista de compras")

lista_de_compras = []
eleccion = "None"

while eleccion not in ["q", "Q"]:
    eleccion = input("\nQue desea comprar? [Q para salir] [V para ver la lista de compras]:\n")
    if eleccion in ["q", "Q"]:
        if not lista_de_compras:
            system("cls")
            print(f"No hay articulos en la lista\n")
        else:
            system("cls")
            print(f"Esta es su lista de compras:\n")
            for elemento in lista_de_compras:
                print(elemento)
            print('')
    elif eleccion in ["v", "V"]:
        if not lista_de_compras:
            system("cls")
            print(f"No hay articulos en la lista")
        else:
            system("cls")
            print(f"Esta es su lista de compras:\n")
            for elemento in lista_de_compras:
                print(elemento)
    else:
        lista_de_compras.append(eleccion)
        print(f"Se ha añadido {eleccion} a la lista de compras\n")
        system("cls")