from os import system

SALIDA = "SALIR"
LISTA = "LISTAR"
ARCHIVO_LISTA = "lista_compra.txt"

def preguntar_producto_usuario():
    return input(f"Introduce el producto [{SALIDA} para salir / {LISTA} para mostrar la lista]:\n")

def crear_lista(lista_compra):
    with open(ARCHIVO_LISTA, "w") as file:
        file.write("\n".join(lista_compra))

def guardar_en_lista(lista_compra, input_usuario):
    system('cls')
    if input_usuario.lower() in [e.lower() for e in lista_compra] or input_usuario.lower() == "":
        system('cls')
        print("Favor elegir un producto que no este en la lista de compras.")
    else:
        lista_compra.append(input_usuario)

def cargar_o_crear_archivo():
    lista_compra = []
    if input("Quieres cargar la ultima lista de compras?[S/N]") in ["s", "S"]:
        try:
            with open(ARCHIVO_LISTA, "r") as a:
                lista_compra = a.read().split("\n")
        except FileNotFoundError:
            print("Archivo de compra no encontrado, se creara un archivo nuevo para la lista.")
    return lista_compra

def main():
    lista_compra = cargar_o_crear_archivo()

    input_usuario = preguntar_producto_usuario()

    while input_usuario.lower() != SALIDA.lower():
        guardar_en_lista(lista_compra, input_usuario)
        print("\n".join(lista_compra))
        input_usuario = preguntar_producto_usuario()

    system('cls')
    crear_lista(lista_compra)

if __name__ == '__main__':
    main()