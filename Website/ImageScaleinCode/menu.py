from PIL import Image

nazwaPliku = "Saitama.jpg"

image = Image.open(nazwaPliku)

width, height = image.size

print("Szerokość obrazu: ", width)
print("Wysokość obrazu: ",height)