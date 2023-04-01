sciezka = "tekst.txt"
slowo = "kot"
 
 
try:
    with open(sciezka, 'r') as f:
        tekst = f.read()
        wystapienia = tekst.count(slowo)
 
    # Wyświetl wynik
    print(f"Liczba wystąpień '{slowo}' w pliku {sciezka} to {wystapienia}.")
except FileNotFoundError:
    print(f"Plik o ścieżce {sciezka} nie został znaleziony.")
except PermissionError:
    print(f"Brak uprawnień do odczytu pliku {sciezka}.")
