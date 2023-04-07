import readchar
from os import system
from random import randint
from time import sleep

#Global variables
POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_MAP_OBJECTS = 11

my_position = [10, 7]
tail_length = 0
map_objects = []
tail = []

#Generating objects 
while len(map_objects) < NUM_MAP_OBJECTS:
    new_position = [randint(0, MAP_WIDTH), randint(0, MAP_HEIGHT)]

    if new_position not in map_objects and my_position != new_position:
        map_objects.append(new_position)
    
#Main loop
while True:
    if my_position in tail:
        system('cls')
        print('You losse')
        sleep(2)
        break
    #Start printing the map
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
            for tail_piece in tail:
                if tail_piece[POS_X] == cordinate_x and tail_piece[POS_Y] == cordinate_y:
                    char_to_draw = "@"
            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = "@"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1
            print(f" {char_to_draw} ", end="")
        print("|")
    #Finish printing the map
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    #Q for quit the game
    print("\nPress [q] for quit")

    if len(map_objects) < 1:
        system('cls')
        print('You win')
        sleep(2)
        break

    direction = readchar.readchar()

    #Directions keys
    if direction in ["w", "W"]:
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction in ["s", "S"]:
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction in ["a", "A"]:
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction in ["d", "D"]:
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction in ["q", "Q"]:
        break
    system('cls')

system('cls')
