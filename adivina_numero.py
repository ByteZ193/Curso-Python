import time
import random

n = random.randint(1,10)

print("Bienbenido a adivina el numero")
time.sleep(2)
print("Debes adivinar cual es el numero que tengo guardado")
time.sleep(2)

num = 0

while num != n:
    num = int(input("Cual es el numero??? "))
    if num == n:
        print("Hurra, adivinaste el numero!!!")
    else:
        print("Lo siento, trata otra vez")