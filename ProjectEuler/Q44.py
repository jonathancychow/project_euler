import numpy as np
from itertools import *

def pentagonal_numbers (n):
    pentagonal_numbers=[]
    for i in range(1, n):
        pentagonal_numbers = np.append(pentagonal_numbers,i*(3*i-1)/2)
    return pentagonal_numbers

numbers = pentagonal_numbers(3000)
combination = combinations (numbers,2)

# answer = []
for k in combination:
    if k[0]+k[1] in numbers and k[1]-k[0] in numbers:
        answer = k
        break 


print(f"Answer: {abs(answer[0]- answer[1])}")