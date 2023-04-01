import f

lista = [ num
         for num in range(-4,10)
        ]
n = 0

for i in lista:
    if i > 0:
        print(i)
        n += i
        print("coś", n)
        

print(f.suma(lista))