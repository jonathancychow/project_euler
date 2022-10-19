from collections import defaultdict
from itertools import *
import time, sys, os

ThisFolder = os.path.dirname(os.path.abspath(__file__))
PathsToAdd = [os.path.abspath(ThisFolder),
              os.path.abspath(os.path.join(ThisFolder,'..'))]
for PathToAdd in PathsToAdd:
    if PathToAdd not in sys.path:
        sys.path.insert(0,PathToAdd)
from PrimeLib import isPrime2

class SpiralPrimes:

    def __init__(self):
        self.sequence = []
        self._threshold = 0.1
        self.answer = 0

    def percentage(self, prime_counter):
        return prime_counter / len(self.sequence)

    def run1(self):

        self.sequence.extend([1,3,5,7,9])
        prime_counter = 3
        diagonal_counter = 4

        # percentage = prime_counter / self.sequence_length
        while self.percentage(prime_counter) > self._threshold:
            for _ in range(4):
                next_number = self.sequence[-1] + diagonal_counter
                prime_counter = prime_counter + 1 if isPrime2(next_number) else prime_counter 
                self.sequence.append(next_number)
            diagonal_counter += 2

        # diagonal counter show the increment to the next spiral, diagonal counter -1 is the current side length
        self.answer = diagonal_counter-1 


if __name__ == "__main__":
    spiral_primes = SpiralPrimes()
    tstart = time.time()
    spiral_primes.run1()
    print('Answer = ',spiral_primes.answer)
    tend = time.time()
    print('Run time for Q58 = ', tend - tstart, 's')

