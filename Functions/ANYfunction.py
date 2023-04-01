numbers1 = [1,3,5,6,7]
numbers2 = [1,3,5,7,9]

def any_even(lista):
    return any([nr % 2 == 0
    for nr in lista])



print(any_even(numbers1))

print(any_even(numbers2))


if (any_even(numbers1)):
    print("Tak jest pażysta")
else:
    print("żadna nie jest pażysta")

if (any_even(numbers2)):
    print("Tak jest pażysta")
else:
    print("żadna nie jest pażysta")