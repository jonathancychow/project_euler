import sys, os, time, glob

ThisFolder = os.path.dirname(os.path.abspath(__file__))
PathsToAdd = [os.path.abspath(ThisFolder),
              os.path.abspath(os.path.join(ThisFolder,'..'))]

for PathToAdd in PathsToAdd:
    if PathToAdd not in sys.path:
        sys.path.insert(0,PathToAdd)

from PrimeLib import *

# prime_text_file = "".join(('Track', '\\', Track, '.csv' ))
# prime_text_file = 'primes-to-100k.txt'
prime_list=[]
text_file = glob.glob("*.txt")
for i in range(len(text_file)):
    prime_text_file = text_file[i]
    with open(prime_text_file, encoding='utf-8-sig') as f:
        # prime_list = f.read().splitlines()
        prime_list.append(f.read().splitlines())

# Flatten prime list, better convert to np array at a later stage
flat_prime_list = []
for sublist in prime_list:
    for item in sublist:
        flat_prime_list.append(item)

# Convert list of string to list of int
flat_prime_list = list(map(int, flat_prime_list))

Pass = []
tstart = time.time()
for i in flat_prime_list:
    Pass.append(isPrime2(i))

if len(Pass) == sum(Pass):
    print('Pass')
else:
    print ('Fail')

tend = time.time()
print('Run time for PrimeLibTest is ', tend - tstart, 's')
