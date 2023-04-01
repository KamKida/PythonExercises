definition = {"kola": "nappuj", 
              "Elden ring": "gra"
              }

print("MENU\n"
      "1.DODAWANIE DEFINICJI\n"
      "2.SZUKAJ DEFINICJI\n"
      "3.UNUŃ DEFINICJE\n"
      "4.ZAKOŃCZ PROGRAM\n"
    )

choic = 0
while True:
    
    choic = int(input("COchcesz zrobić: "))
    
    if choic == 1:
        while True:
            key = input("Podaj słowo definiowane: ")
            defi = input("Podaj definicje słowa: ")
            definition[key]= defi
            choic2 = input("Czy chceszx kontynuować? (y/n): ")
            if choic2 == "y":
                continue
            elif choic2 == "n":
                break
        
    
    elif choic == 2:
        while True:
            key = input("Podaj słowo którego szukasz: ")
            print(key," : ",definition[key])
            choic2 = input("Czy chceszx kontynuować? (y/n): ")
            if choic2 == "y":
                continue
            elif choic2 == "n":
                break
        
    
    elif choic == 3:
        while True:
            key = input("Podaj słowo które chcesz usunąć: ")
            
            definition.pop(key)

            print("Definicja ",key," została usunięta.")
            
            choic2 = input("Czy chceszx kontynuować? (y/n): ")
            if choic2 == "y":
                continue
            elif choic2 == "n":
                break
    
    elif  choic == 4:
        break

print(definition)