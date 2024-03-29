from os import system
from string import ascii_uppercase
from string import ascii_lowercase

#Ejejcicio 1: Crea una funcion que reciba una lista de strings como entrada y te diga cual es la más larga de todas
def most_long_string(*args):
    return max(args, key=len)
    

#Ejecicio 2: Crea una función que sume una lista de números, no se vale usar la función sum()
def plus(*args):
    suma = 0
    for e in args:
        suma += e
    return print(suma)

#Ejercicio 3: Crea una función que te de True como resultado si el número pasado como argumento es impar
def odd(n):
    if n % 2 == 1:
        return True
    return False

#Ejercicio 4: Crea una función que pregunte al usuario si esta seguro o no, y devuelva los valores "True" o "False"
# dependiendo de si el usuario está seguro.
def question():
    q = (input("Estas seguro (si/no)?\n")).lower()
    while q not in ["si", "no"]:
        system('cls')
        q = (input("Favor elegir si o no; estas seguro (si/no)?\n")).lower()
        if q == "no":
            return False
    return True

#Ejercicio 5: Crea una función que convierta toda una string en mayusculas, no vale usar el método upper()
def upper(string):
    result = ""
    for s in string:
        if(ord(s) >= 97):
            result += chr(ord(s) - 32)
        else:
            result += s
    return print(result)

# Ejercicio 6: Crea una función que reciba como argumento un número del 1 al 100 a adivinar y que le pregunte al usuario
# que adivine el número. El código se ejecutará hasta que el usuario adivine.
def guess(n):
    guess = input("Adivine el numero 1 al 100, favor introducir solo numeros:\n")
    while guess in ascii_uppercase or guess in ascii_lowercase or guess != str(n):
        system('cls')
        guess = input("No adivinaste!!, vuelve a intentarlo; favor introducir solo numeros del 1 al 100:\n")
    system('cls')
    return print("Adivinaste!!!")

# Ejercicio 7:Crea una función que dada una lista de la compra definida fuera de la función, permita al usuario añadir un
# nuevo item asegurandose que no exista anteriormente en la lista.
def shopping(adding):
    add = ""
    print(f"Esta es la lista de compras: {adding}")
    q = input("Desea agregar algo mas? (si/no)\n").lower()
    while q not in ["si", "no"]:
        system('cls')
        q = (input("Favor elegir si o no; quieres agregar algo mas (si/no)?\n")).lower()
    if q == "si":
        system('cls')
        while add not in ["Q", "q"]:
            add = input("Que desea agregar? precione Enter cada que escriba un articulo para guardar (q para salir):\n")
            adding.append(add)
    elif q == "no":
        system('cls')
        return print(f"Su lista quedo asi: {adding}")
    adding.pop()
    return print(f"Su lista quedo asi: {adding}")

def main():
    shopping_list = ["Aguacate", "Azucar", "Pan", "Arroz", "Leche"]
    print(most_long_string('hola', 'esto no tiene sentido', 'adios', 'Supercalifragilisticoespialidoso'))
    #plus(2, 2)
    #print(odd(2))
    #print(question())
    #upper("Hola klk Edwin")
    #guess(3)
    #shopping(shopping_list)

if __name__ == '__main__':
    main()
