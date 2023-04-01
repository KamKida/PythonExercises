def read_content_of_file(path):
    try:
        with open(path, "r", encoding="UTF-8") as file:
            return file.read()
    except FileNotFoundError:
         print("Nie znaleziono pliku, podaj prawidłową ścieżkę")
