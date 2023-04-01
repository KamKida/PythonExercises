import time

def sumuj_do(liczba):

    suma=0

    for liczba in range(1,liczba+1):
    
        suma+=liczba
    
    return suma

def sumuj_do2(liczba):
    return sum( [liczby for liczby in range(1,liczba+1)])

def sumuj_do3(liczba):
    return sum( {liczby for liczby in range(1,liczba+1)})

def sumuj_do4(liczba):
    return sum( (liczby for liczby in range(1,liczba+1)))
    
def sumuj_do5(liczba):
  return (1 + liczba) / 2 * liczba
    
def finish_timer(start):
    end = time.perf_counter()
    return end - start

def function_performance(func, arg, how_many_times = 1):
    
    suma = 0 
    
    for _ in range(0,how_many_times+1):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        suma = suma + (end - start)

    return suma


print(function_performance(sumuj_do,5000, 500))
print(function_performance(sumuj_do2,5000, 500))
print(function_performance(sumuj_do3,5000))
print(function_performance(sumuj_do4,5000))
print(function_performance(sumuj_do5,5000))



