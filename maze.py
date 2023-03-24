import readchar
from os import system

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
my_position = [10, 7]

while True:
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for cordinate_x in range(MAP_WIDTH):
            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                print(" @ ", end="")
            else:
                print("   ", end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print("\nprecione [q] para salir")

    direction = readchar.readchar()

    if direction in ["w", "W"]:
        my_position[POS_Y] -= 1
    elif direction in ["s", "S"]:
        my_position[POS_Y] += 1
    elif direction in ["a", "A"]:
        my_position[POS_X] -= 1
    elif direction in ["d", "D"]:
        my_position[POS_X] += 1
    elif direction in ["q", "Q"]:
        break
    system('cls')

system('cls')
