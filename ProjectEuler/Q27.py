import time
from primelib.primelib import isPrime2


# Define the upper and the lower limit of the check
limit = 1000
# Initial values
n = 0
max_prime = 0
max_i = 0
max_j = 0
quartic_sum = 2
tstart = time.time()

for i in range (-limit, limit,1):
    for j in range (-limit, limit,1):
        while isPrime2(quartic_sum)==True:
            quartic_sum = n**2 + i * n + j
            n += 1

        if n-1 > max_prime:
            max_prime = n-1
            max_i = i
            max_j = j

        # reset n and quartic_sum to initial value
        quartic_sum = 2
        n = 0


print (max_j)
print (max_i)
print ('Answer = ',max_j* max_i)
tend = time.time()
print('Run time for Q27 =',tend-tstart,'s')