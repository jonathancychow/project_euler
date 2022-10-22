
import math
import datetime 

from primelib.primelib import generate_prime_list2


max_value = 10000
prime_list = generate_prime_list2(max_value)

def check_perfect_square(number)-> bool:
    # https://djangocentral.com/python-program-to-check-if-a-number-is-perfect-square/
    if int(number) in [0]: 
        return False
    
    root = math.sqrt(number)
    return int(root + 0.5) ** 2 == number 

def find_largest_prime_index(number, prime_list):
    i = 0 
    while number > prime_list[i]:
        i += 1 
    
    return i-1

def odd_composite_number(max_value) ->list:
    prime_list = generate_prime_list2(max_value)
    odd_number = set(range(1, max_value, 2))

    return list(odd_number - set(prime_list))

start_time = datetime.datetime.now()
answer = None

for number in odd_composite_number(max_value):   
    
    found = False
    max_prim_index = find_largest_prime_index(number, prime_list)

    for prim_index in range(max_prim_index, -1, -1):
        
        if check_perfect_square((number - prime_list[prim_index])/2):
            found = True
            break
    
        if prim_index == 0 and found is False:
            answer = number
            break

    if answer:
        break
time_taken = datetime.datetime.now() - start_time  

print(f"Answer : {answer}, time taken {time_taken} s")
    