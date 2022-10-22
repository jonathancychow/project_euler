from itertools import *
import time

from primelib.primelib import isPrime2

def pandigital_prime(n):

    permutation = list(permutations(range(1, n + 1),n))
    numbers = []
    for k in permutation:
        number = 0
        for i in range(len(k)):
            number = number + k[i] * 10**(len(k)-1-i)
        numbers.append(number)
    numbers.sort(reverse = True)
    answer = 0
    for i in range(len(numbers)):
        if isPrime2(numbers[i]):
            answer = numbers[i]
            break
        #sort all the number
        #check from the biggest number, find the first prime number
    if answer == 0:
        answer = pandigital_prime(n-1)

    return answer
tstart = time.time()
print('Answer = ',pandigital_prime(9))
tend = time.time()
print('Run time for Q41= ',tend-tstart,'s')
