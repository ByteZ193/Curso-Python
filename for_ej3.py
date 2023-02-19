numero = int(input("Introduzca el numero al cual quiere saber la tabla de mutlipicar:\n"))

for e in range(0, 13):
    if (e * numero) % 2 == 0:
        print(f"{numero} x {e} = {numero * e}")