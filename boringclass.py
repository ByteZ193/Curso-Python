from os import system

#Ejejcicio 1: Crea una funcion que reciba una lista de strings como entrada y te diga cual es la más larga de todas
def most_long_string(*args):
    long = ''
    i = 0
    for e in args:
        if len(e) > len(long):
            long = e
            i += 1
    return print(f"La string mas larga es la {i} '{long}' con {len(long)} caracteres.")

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

def main():
    #most_long_string('hola', 'esto no tiene sentido', 'adios', 'Supercalifragilisticoespialidoso')
    #plus(2, 2)
    #print(odd(2))
    print(question())

if __name__ == '__main__':
    main()
