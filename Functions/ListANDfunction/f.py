def suma(list):
    new_lis = []
    for number in list:
        if number >0:
            new_lis.append(number)
    return sum(new_lis)
