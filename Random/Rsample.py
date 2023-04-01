import random

def choice_random_numbers(amount, total_amount):
    print(random.sample(range( total_amount+1),amount))



choice_random_numbers(6, 49)