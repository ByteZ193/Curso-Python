print("Vamos a preparar colacao!!!")

leche = input("Hay leche??? (escribe s para si o n para no): ")

if leche.lower() == "s":
    print("Bien hay leche!!!")

    colacao = input("Hay colacao??? (escribe s para si o n para no): ")

    if colacao.lower() == "s":
        print("Bien hay Colacao!!!!")
        
        print("Pudiste hacer leche con colacao!!!!")
    else:
        print("No hay colacao, no puedes preparar leche con colacao :(")
    
else:
        print("No hay leche, no puedes preparar leche con colacao :(")
