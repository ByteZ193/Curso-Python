from os import system

print("Bienbenido al test de quesos\n")

score = 0

p1 = int(input("Que haces cuando vez una tabla de quesos?"
               "\n1- Salgo corriendo"
               "\n2- Puebo uno de los quesos o incluso varios"
               "\n3- No puedo evitar devorarla\n"))

while p1 not in range(1, 4):
    system("cls")
    p1 = int(input("Elija solo las opciones marcadas (1, 2, 3)!!!\n"
                   "Que haces cuando vez una tabla de quesos?"
                   "\n1- Salgo corriendo"
                   "\n2- Puebo uno de los quesos o incluso varios"
                   "\n3- No puedo evitar devorarla\n"))

if p1 == 1:
    score += 0
elif p1 == 2:
    score += 5
elif p1 == 3:
    score += 10

system("cls")

p2 = int(input("Como te gusta la hamburguesa? "
               "\n1- Sin queso"
               "\n2- Con queso"
               "\n3- Pan y queso\n"))

while p2 not in range(1, 4):
    system("cls")
    p2 = int(input("Elija solo las opciones marcadas (1, 2, 3)!!!\n"
                   "Como te gusta la hamburguesa? "
                   "\n1- Sin queso"
                   "\n2- Con queso"
                   "\n3- Pan y queso\n"))

if p2 == 1:
    score += 0
elif p2 == 2:
    score += 5
elif p2 == 3:
    score += 10

system("cls")

p3 = int(input("Eres intolerante a la lactosa? \n"
               "1- Si"
               "\n2- A veces"
               "\n3- No\n"))

while p3 not in range(1, 4):
    system("cls")
    p3 = int(input("Elija solo las opciones marcadas (1, 2, 3)\n"
                   "Eres intolerante a la lactosa? \n"
                   "\n1- Si"
                   "\n2- A veces"
                   "\n3- No\n"))

if p3 == 1:
    score += 0
elif p3 == 2:
    score += 5
elif p3 == 3:
    score += 10

system("cls")

if score >= 25:
    print(f"Tu puntuacion es {score}, te fascina el queso")
elif 15 <= score < 25:
    print(f"Tu puntuacion es {score}, te gusta un poco el queso")
elif score < 15:
    print(f"Tu puntuacion es {score}, no te gusta el queso")
