import sys, os, time, glob
import numpy as np
ThisFolder = os.path.dirname(os.path.abspath(__file__))
PathsToAdd = [os.path.abspath(ThisFolder),
              os.path.abspath(os.path.join(ThisFolder,'..'))]

for PathToAdd in PathsToAdd:
    if PathToAdd not in sys.path:
        sys.path.insert(0,PathToAdd)

from PrimeLib import *

text_file = glob.glob("*.txt")
prime_list = np.array([])
for i in range(len(text_file)):
    prime_text_file = text_file[i]
    with open(prime_text_file, encoding='utf-8-sig') as f:
        prime_list = np.append(prime_list,f.read().splitlines())

# Convert list of string to list of int
prime_list = list(map(int, prime_list))

Pass = []
tstart = time.time()
for i in prime_list:
    Pass.append(isPrime2(i))

if len(Pass) == sum(Pass):
    print('Pass')
else:
    print ('Fail')

tend = time.time()
print('Run time for PrimeLibTest is ', tend - tstart, 's')
