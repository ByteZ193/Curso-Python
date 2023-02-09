from os import system

print("Bienvenido al conversor de libras inlgesas a pesos dominicanos!!!!")

op = int(input("A que quiere convertir? (libras - 1, pesos - 2)\n"))

while op not in range(1,3):
    system("cls")
    op = int(input("Debe de elegir las opciones 1 o 2\n"
                   "A que quiere convertir? (libras - 1, pesos - 2)\n"))

system("cls")

if op == 1:
    pesos = float(input("Cuantos pesos quieres convertir a libras? "))
    libras = pesos / 60.64
    print(f"{pesos} Pesos en libras serian {round(libras, 2)} libras")
elif op == 2:
    libras = float(input("Cuantas libras quieres convertir a pesos? "))
    pesos = libras * 60.64
    print(f"{libras} Libras en pesos serian {round(pesos, 2)} pesos")
