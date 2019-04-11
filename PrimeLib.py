import math


def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True;
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
    return True


def isPrime2(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False
    return True

# From zacharydenton
# https://github.com/zacharydenton/euler/blob/master/047/consecutive-factors.py
def factorisePrime(n):
    if n < 1:
        raise ValueError('fact() argument should be >= 1')
    if n == 1:
        return []  # special case
    res = []
    # iterate over all even numbers first.
    while n % 2 == 0:
        res.append(2)
        n //= 2
    # try odd numbers up to sqrt(n)
    limit = math.sqrt(n+1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.append(i)
            n //= i
            limit = math.sqrt(n+i)
        else:
            i += 2
    if n != 1:
        res.append(n)
    return res

def chekcUniquePrimeFactor(list):
    j = 0
    distinct_prime_factor=[]
    distinct_prime_factor.append(list[0])
    for i in range(0,len(list),1):
        if len(list)>1 and i!=0:
            if list[i] == list[i-1]:
                distinct_prime_factor[j] = distinct_prime_factor[j] * list[i]
            else:
                j += 1
                distinct_prime_factor.append(list[i])
    return distinct_prime_factor

def generate_prime_list(n):
    prime_list = []
    for i in range(2, n):
        if isPrime2(i):
            prime_list.append(i)
    return prime_list

def generate_prime_list2(n):
    prime_list = []
    i=2
    while len(prime_list)<n:
       if isPrime2(i)==1:
           prime_list.append(i)
           i = i+1
       else:
           i = i+1
    return prime_list