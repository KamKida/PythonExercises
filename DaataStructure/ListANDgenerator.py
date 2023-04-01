lista = [
            number
            for number in range(100, 471)
            if (number % 7 == 0) and (number % 5 == 0)
        ]

print(lista)


generator = (
            number
            for number in range(100, 471)
            if (number % 7 == 0) and (number % 5 == 0)
            )


print(generator)


