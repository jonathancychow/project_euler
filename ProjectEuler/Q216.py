from itertools import *
import time, sys, os
ThisFolder = os.path.dirname(os.path.abspath(__file__))
PathsToAdd = [os.path.abspath(ThisFolder),
              os.path.abspath(os.path.join(ThisFolder,'..'))]
for PathToAdd in PathsToAdd:
    if PathToAdd not in sys.path:
        sys.path.insert(0,PathToAdd)
from PrimeLib import *

class Primality:

    def __init__(self):
        self.number =[]
        # self.number.append(2)
        self.primenumber = []
        self.sequence = []
        self.sequence_sum = []

    def run1(self, n):


        # self.generate_prime_list(n)
        # self.primenumber = generate_prime_list(2*n**2-1)
        count = 0
        for i in range(n):
            if isPrime2(2*i**2-1):
                count += 1

        return count


if __name__ == "__main__":
    Run = Primality()
    tstart = time.time()
    print((Run.run1(n=50000000)))
    tend = time.time()
    print('Run time for Q50= ', tend - tstart, 's')



