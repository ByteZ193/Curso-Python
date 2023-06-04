import readchar
from os import system
from random import randint
from time import sleep

# Global variables
POS_X = 0
POS_Y = 1
NUM_MAP_OBJECTS = 3

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
map_objects = []
new_position = []
object_in_cell = []

pokemon = ["Pikachu", "Charmander", "Bulbasaur"]
VIDA_POKEMON_INICIAL = 80
VIDA_SQUIRTLE_INICIAL = 110
pokemon_interator = 0

vida_pokemon = VIDA_POKEMON_INICIAL
vida_squirtle = VIDA_SQUIRTLE_INICIAL

# Create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# Main loop
while True:
    # Generating objects
    if len(map_objects) < NUM_MAP_OBJECTS:
        new_position = [randint(0, MAP_WIDTH - 1), randint(1, MAP_HEIGHT - 1)]

        if new_position not in map_objects and new_position != my_position and obstacle_definition[new_position[POS_Y]][
                new_position[POS_X]] == " ":
            map_objects.append(new_position)

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
            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = "@"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    system('cls')
                    print("\nInicia una batalla pokemon!!!!!")
                    sleep(2)
                    while vida_pokemon > 0 and vida_squirtle > 0:
                        print(pokemon[pokemon_interator])
                        print("[" + "*" * int(vida_pokemon / 10) + " " * int(
                            8 - vida_pokemon / 10) + "]" + f" {vida_pokemon}/{VIDA_POKEMON_INICIAL} PS")
                        print("Squirtle")
                        print("[" + "*" * int(vida_squirtle / 10) + " " * int(
                            9 - vida_squirtle / 10) + "]" + f" {vida_squirtle}/{VIDA_SQUIRTLE_INICIAL} PS")

                        print(f"Turno de {pokemon[pokemon_interator]}")
                        sleep(2)
                        system('cls')

                        ataque_pokemon = randint(1, 2)

                        if ataque_pokemon == 1 and pokemon[pokemon_interator] == "Pikachu":
                            print(f"\n{pokemon[pokemon_interator]} ataca con bola voltio 15 de potencia\n")
                            vida_squirtle -= 15
                        elif ataque_pokemon == 1 and pokemon[pokemon_interator] == "Charmander":
                            print(f"\n{pokemon[pokemon_interator]} ataca con ascuas 15 de potencia\n")
                            vida_squirtle -= 15
                        elif ataque_pokemon == 1 and pokemon[pokemon_interator] == "Bulbasaur":
                            print(f"\n{pokemon[pokemon_interator]} ataca con latigo cepa 15 de potencia\n")
                            vida_squirtle -= 15
                        elif ataque_pokemon == 2:
                            print(f"\n{pokemon[pokemon_interator]} ataca con arañaso 10 de potencia\n")
                            vida_squirtle -= 10

                        if vida_squirtle <= 0:
                            continue

                        sleep(1)

                        ataque_squirtle = None
                        while ataque_squirtle not in ["a", "p", "b"]:
                            print(pokemon[pokemon_interator])
                            print("[" + "*" * int(vida_pokemon / 10) + " " * int(
                                8 - vida_pokemon / 10) + "]" + f" {vida_pokemon}/{VIDA_POKEMON_INICIAL} PS")
                            print("Squirtle")
                            print("[" + "*" * int(vida_squirtle / 10) + " " * int(
                                9 - vida_squirtle / 10) + "]" + f" {vida_squirtle}/{VIDA_SQUIRTLE_INICIAL} PS")
                            ataque_squirtle = input('\nTu turno, que ataque elegiras???\nA - Pistola agua 20 de '
                                                    'potencia\nP - Placaje 10 de potencia\nB - Burbujas 5 de potencia\n\n')
                            system('cls')

                        if ataque_squirtle.lower() == "a":
                            print("\nSquirtle ataca con pistola agua")
                            vida_pokemon -= 20
                        elif ataque_squirtle.lower() == "p":
                            print("\nSquirtle ataca con placaje")
                            vida_pokemon -= 10
                        elif ataque_squirtle.lower() == "b":
                            print("\nSquirtle ataca con burbujas")
                            vida_pokemon -= 5
                        sleep(2)
                        system('cls')

                    if vida_pokemon == 0:
                        print("Squirtle gana!!!")
                        sleep(2)
                        system('cls')
                    elif vida_squirtle == 0:
                        print(f"{pokemon[pokemon_interator]} gana!!!")
                        system('cls')
                    vida_pokemon = VIDA_POKEMON_INICIAL
                    system('cls')
                    pokemon_interator += 1
                    sleep(1)
                    NUM_MAP_OBJECTS -= 1
            if obstacle_definition[cordinate_y][cordinate_x] == "#":
                char_to_draw = "#"
            print(f" {char_to_draw} ", end="")
        print("|")
    # Finish printing the map
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    # Ending game loop
    if pokemon_interator >= 3:
        system('cls')
        print("You win")
        sleep(2)
        break
    # Q for quit the game
    print("\nPress [q] for quit")

    direction = readchar.readchar()
    new_position = None

    # Directions keys
    if direction in ["w", "W"]:
        new_position = [my_position[POS_X],
                        (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction in ["s", "S"]:
        new_position = [my_position[POS_X],
                        (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction in ["a", "A"]:
        new_position = [(my_position[POS_X] - 1) %
                        MAP_WIDTH, my_position[POS_Y]]

    elif direction in ["d", "D"]:
        new_position = [(my_position[POS_X] + 1) %
                        MAP_WIDTH, my_position[POS_Y]]

    elif direction in ["q", "Q"]:
        break

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

    system('cls')
system('cls')
