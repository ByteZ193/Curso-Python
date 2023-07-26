import os

def main():
    desktop_path = os.environ['USERPROFILE'] + '\\Desktop\\'
    a = open(desktop_path + "PARA TI.txt", "w")
    a.write("Soy un hacker")
    a.close()


if __name__ == "__main__":
    main()
