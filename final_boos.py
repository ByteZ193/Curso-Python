from os import system
from random import randint

decision1 = 0
palo = None
numero = randint(100, 999)

while decision1 not in [1, 2]:
    system('cls')
    print("\nBienbenido al escape de la mazmorra\n")
    decision1 = int(input("Fuiste atrapado por unos orcos y estas apunto de escapar con tu compañero. Sales de la camara\n"
                          "en donde estaban atrapados y salen corriendo por el pasillo, y encuentran una puerta\n"
                          "semi-abierta, y una escotilla por donde pueden saltar. Que deciden hacer?\n\n 1- Van por la "
                          "puerta semi-abierta.\n 2- Van y saltan por la escotilla.\n\n"))

if decision1 == 1:
    decision2 = 0
    while decision2 not in [1, 2]:
        system('cls')
        decision2 = int(input(f"Te encuentras con un guardia que tiene un sombrero vikingo con el numero {numero}, "
                              "que haras?\n\n 1- Sales corriendo.\n 2- Te haces el dormido.\n\n"))
    if decision2 == 2:
        system('cls')
        print("Moriste ;(, el guardia te asesino\n")
    else:
        system('cls')
        codigo = int(input("Llegaste hasta una puerta que pide un codigo de tres numeros:\n"))

        if codigo == numero:
            system('cls')
            print("Lograste salir de la mazmorra :)\n")
        else:
            print("Moriste ;(, el guardia te alcanzo y te asesino\n")
else:
    system('cls')
    decision3 = 0
    while decision3 not in [1, 2]:
        system('cls')
        decision3 = int(input("Caes en una zona inundada, el agua te llegas a las rodillas, sigues caminando durante una "
                              "media hora hasta que llegas a un claro cuya luz viene de arriba, como si fuera una "
                              f"alcantarilla con un numero {numero} en el centro, y vez un palo junto a ella. "
                              "Que decides?\n\n 1- Coger el palo.\n 2- No coger el palo.\n\n"))

    if decision3 == 1:
        system('cls')
        palo = True
        decision4 = int(input("Subes por la alcantarilla y te encuentras con una rata de 2 metros que se dice llamar "
                              "Splinter, ella te dice que le digas el numero secreto para dejarte avanzar a la salida. "
                              "Cual es el numero secreto?\n\n"))
        if decision4 == numero:
            system('cls')
            print("Bien!!!, adivinaste!!!, Splinter te muestra el camino a seguir, y logras salir a salvo de la mazmorra.\n"
                  "Felicidades!!!\n")
        else:
            system('cls')
            print("Splinter te dice que vallas por un camino secreto que estaba detras de una pared, que por ahi esta la "
                  "salida. Sigues avanzando, y cuando vez una salida, pisas una trampa la cual hace que se comience a "
                  "cerrar la puerta, pero usas el palo que recogiste anteriormente y lograste atascar la puerta para poder "
                  "salir. Felicidades!!!, Saliste de la mazmorra.\n")
    else:
        system('cls')
        palo = False
        decision4 = int(input("Subes por la alcantarilla y te encuentras con una rata de 2 metros que se dice llamar "
                              "Splinter, ella te dice que le digas el numero secreto para dejarte avanzar a la salida. "
                              "Cual es el numero secreto?\n\n"))
        if decision4 == numero:
            system('cls')
            print("Bien!!!, adivinaste!!!, Splinter te muestra el camino a seguir, y logras salir a salvo de la mazmorra.\n"
                  "Felicidades!!!\n")
        else:
            system('cls')
            print("Splinter te dice que vallas por un camino secreto que estaba detras de una pared, que por ahi esta la "
                  "salida. Sigues avanzando, y cuando vez una salida, pisas una trampa la cual hace que se comience a "
                  "cerrar la puerta, al no tener con que evitar que la puerta se cierre, no lograste escapar. Moriste de "
                  "hambre :(\n")
