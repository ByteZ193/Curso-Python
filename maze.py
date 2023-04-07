import readchar
from os import system

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
my_position = [10, 7]
map_objects = [[2, 3], [5, 4], [3, 4], [7, 8], [9, 10], [5, 9]]

while True:
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for cordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            object_in_cell = None
            for map_object in map_objects:
                if map_object[POS_X] == cordinate_x and map_object[POS_Y] == cordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object
            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = "@"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
            print(f" {char_to_draw} ", end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print("\nprecione [q] para salir")

    direction = readchar.readchar()

    if direction in ["w", "W"]:
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction in ["s", "S"]:
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction in ["a", "A"]:
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction in ["d", "D"]:
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction in ["q", "Q"]:
        break
    system('cls')

system('cls')
