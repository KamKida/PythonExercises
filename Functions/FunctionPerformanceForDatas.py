import time 

def function_performance(func, how_many_times = 1, *arg,):
    sum = 0

    for _ in  range(0, how_many_times):
        start = time.perf_counter()
        func (*arg)
        end  = time.perf_counter()
        sum = sum + (end - start)
    
    return sum


setContainer = {
                i
                for i in  range(1000)
                }   

listContainer = [
                i 
                for i in range(1000)
                ]

def is_element_in(what_value, container):
    if what_value in container:
        return True
    else:
        return False
    
print(function_performance(is_element_in,50,450, setContainer,))
print(function_performance(is_element_in,50,450, listContainer,))