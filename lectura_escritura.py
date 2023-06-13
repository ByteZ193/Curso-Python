from os import system

SALIDA = "SALIR"
LISTA = "LISTAR"

def preguntar_producto_usuario():
    return input(f"Introduce el producto [{SALIDA} para salir][{LISTA} para listar productos]:\n")

def preguntar_nombre_usuario():
    return input(f"Introduce de la lista [{SALIDA} para salir]:\n")

def crear_lista(nombre, lista_compra):
    with open(f"{nombre}.txt", "w") as file:
        file.write(f"{lista_compra}\n")

def main():
    lista_compra = []
    lista_productos = ["Salami", "Salmon", "Pan", "Arroz", "Leche", "Pasta"]

    input_usuario = preguntar_producto_usuario()

    while input_usuario != SALIDA:
        if input_usuario == LISTA:
            system('cls')
            print(", ".join(lista_productos))
            input_usuario = preguntar_producto_usuario()
        else:
            if input_usuario not in lista_productos:
                system('cls')
                print("Favor elegir un producto de la lista de productos")
                input_usuario = preguntar_producto_usuario()
            else:
                system('cls')
                lista_compra.append(input_usuario)
                print(", ".join(lista_compra))
                input_usuario = preguntar_producto_usuario()

    system('cls')
    input_nombre_lista = preguntar_nombre_usuario()
    crear_lista(input_nombre_lista, lista_compra)

if __name__ == '__main__':
    main()