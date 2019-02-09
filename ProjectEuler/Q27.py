import time, numpy, sys, os

ThisFolder = os.path.dirname(os.path.abspath(__file__))
PathsToAdd = [os.path.abspath(ThisFolder),
              os.path.abspath(os.path.join(ThisFolder,'..'))]

for PathToAdd in PathsToAdd:
    if PathToAdd not in sys.path:
        sys.path.insert(0,PathToAdd)

from PrimeLib import *

limit = 1603
n = 0
max_prime = 0
max_i = 0
max_j = 0
quartic_sum = 2

for i in range (-limit, limit,1):
    for j in range (-limit, limit,1):
        while isPrime2(quartic_sum)==True & bool(quartic_sum > 0)==True :
            quartic_sum = n**2 + i * n + j
            n += 1

        if n-1 > max_prime:
            max_prime = n-1
            max_i = i
            max_j = j

        n = 0
        quartic_sum = 2


print (max_j)
print (max_i)
print (max_j* max_i)