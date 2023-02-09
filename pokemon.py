from random import randint
from os import system
from time import sleep

vida_pikachu = 80
vida_squirtle = 90

while vida_pikachu > 0 and vida_squirtle > 0:

    print("Pikachu")
    print("[" + "*" * int(vida_pikachu / 10) + " " * int(8 - vida_pikachu / 10) + "]" + f" {vida_pikachu} PS")
    print("Squirtle")
    print("[" + "*" * int(vida_squirtle / 10) + " " * int(9 - vida_squirtle / 10) + "]" + f" {vida_squirtle} PS")

    print("Turno de pikachu")
    sleep(3)
    system('cls')

    ataque_pikachu = randint(1, 2)

    if ataque_pikachu == 1:
        print("\nPikachu ataca con bola voltio 15 de potencia\n")
        vida_squirtle -= 15
    elif ataque_pikachu == 2:
        print("\nPikachu ataca con onda trueno 10 de potencia\n")
        vida_squirtle -= 10
    
    if vida_squirtle <= 0:
        continue
    
    sleep(2)

    ataque_squirtle = None
    while ataque_squirtle != "a" and ataque_squirtle != "p" and ataque_squirtle != "b":
        print("Pikachu")
        print("[" + "*" * int(vida_pikachu / 10) + " " * int(8 - vida_pikachu / 10) + "]" + f" {vida_pikachu} PS")
        print("Squirtle")
        print("[" + "*" * int(vida_squirtle / 10) + " " * int(9 - vida_squirtle / 10) + "]" + f" {vida_squirtle} PS")
        ataque_squirtle = input('\nTu turno, que ataque elegiras???\nA - Pistola agua 20 de potencia\nP - Placaje 10 de potencia\nB - Burbujas 5 de potencia\n\n')
        system('cls')

    if ataque_squirtle.lower() == "a":
        print("\nSquirtle ataca con pistola agua")
        vida_pikachu -= 20
    elif ataque_squirtle.lower() == "p":
        print("\nSquirtle ataca con placaje")
        vida_pikachu -= 10
    elif ataque_squirtle.lower() == "b":
        print("\nSquirtle ataca con burbujas")
        vida_pikachu -= 5
    sleep(3)
    system('cls')

if vida_pikachu == 0:
    print("Squirtle gana!!!")
    sleep(3)
    system('cls')
elif vida_squirtle == 0:
    print("Pikachu gana!!!")
    system('cls')

sleep(2)
