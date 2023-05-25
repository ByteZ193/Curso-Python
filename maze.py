import readchar
from os import system
from random import randint
from time import sleep

# Global variables
POS_X = 0
POS_Y = 1
NUM_MAP_OBJECTS = 11

obstacle_definition = """\
####      #######     #####
                           
                           
###############       #####
###############       #####
                           
                           
#######              ######
                           
                           
####################    ###
                           
                           
#####    #####            #
                           
######                  ###
          #######          
####                  #####
####      #######     #####\
"""

my_position = [0, 1]
tail_length = 0
map_objects = []
tail = []
new_position = []
object_in_cell = []

# Create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# Main loop
while True:
    # Generating objects
    while len(map_objects) < NUM_MAP_OBJECTS:
        new_position = [randint(0, MAP_WIDTH - 1), randint(1, MAP_HEIGHT - 1)]

        if new_position not in map_objects and new_position != my_position and obstacle_definition[new_position[POS_Y]][
            new_position[POS_X]] == " " and my_position != object_in_cell:
            map_objects.append(new_position)

    if my_position in tail:
        system('cls')
        print('You losse')
        sleep(1)
        break
    # Start printing the map
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for cordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None
            for map_object in map_objects:
                if map_object[POS_X] == cordinate_x and map_object[POS_Y] == cordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object
            for tail_piece in tail:
                if tail_piece[POS_X] == cordinate_x and tail_piece[POS_Y] == cordinate_y:
                    char_to_draw = "@"
                    tail_in_cell = tail_piece
            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = "@"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1
            if obstacle_definition[cordinate_y][cordinate_x] == "#":
                char_to_draw = "#"
            print(f" {char_to_draw} ", end="")
        print("|")
    # Finish printing the map
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print(map_objects)
    print(my_position)
    # Q for quit the game
    print("\nPress [q] for quit")

    direction = readchar.readchar()
    new_position = None

    # Directions keys
    if direction in ["w", "W"]:
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction in ["s", "S"]:
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction in ["a", "A"]:
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction in ["d", "D"]:
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction in ["q", "Q"]:
        break

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position

    system('cls')
system('cls')
