import f_pole
from time import sleep
import os
from enum import IntEnum

Menu_Figury = IntEnum('Menu_Figury', 'Prostokat Kwadrat Trójkąt Trapez Koła')

clear = lambda: os.system('cls')

while True:

    print("Menu\n"
        "Wiram, jakie pole chcesz policzyć? :\n"
        "1.Prostokąt.\n"
        "2.Kwadrat.\n"
        "3.Trójkąt.\n"
        "4.Trapez.\n"
        "5.Koła.\n"
        "6.Wyjdź.\n")





    wyb = input("WYBOR: ")
    if wyb == Menu_Figury.Prostokat:
            a = int(input("Podaj 1 bok prostokąta: "))
            b = int(input("Podaj 1 bok prostokąta: "))
            
            x = f_pole.prostokąt(a,b)
            
            clear()
            
            print("pole: ",x)
            sleep(3)
            clear()
            continue

    elif wyb == Menu_Figury.Kwadrat:
            a = int(input("Podaj bok kwadratu: "))
            
            x = f_pole.kwadrat(a)
            
            clear()
            
            print("Pole: ",x)
            
            sleep(3)
            clear()
            continue

    elif wyb == Menu_Figury.Trójkąt:
            a = int(input("Podaj bok trójkąta: "))
            h = int(input("Podaj wysokość trójkata: "))
            
            x = f_pole.trójkąt(a,h)

            clear()

            print("Pole: ",x)

            sleep(3)
            clear()
            continue

    elif wyb == Menu_Figury.Trapez:
            a = int(input("Podaj pierwszy bok trapezu: "))
            b = int(input("Podaj drugi bok trapezu: "))
            h = int(input("Podaj wysokość trapezu: "))

            x = f_pole.trapez(a,b,h)

            clear()

            print("Pole: ",x)

            sleep(3)
            clear()
            continue

    elif wyb == Menu_Figury.Koła:
            a = int(input("Podaj promień koła: "))

            x = f_pole.koło(a)

            clear()

            print("Pole: ",x)

            sleep(3)
            clear()
            continue

    elif wyb == "6":
            print("Dziękuje za uwage ")
            sleep(3)
            quit()
        
    else:
            print("Wybierz liczbe z menu")

