from itertools import *
import time, sys, os
ThisFolder = os.path.dirname(os.path.abspath(__file__))
PathsToAdd = [os.path.abspath(ThisFolder),
              os.path.abspath(os.path.join(ThisFolder,'..'))]
for PathToAdd in PathsToAdd:
    if PathToAdd not in sys.path:
        sys.path.insert(0,PathToAdd)
from PrimeLib import *

class prime_pair_sum:

    def __init__(self):
        self.combination =[]
        # self.number.append(2)
        self.primenumber = []
        self.best = float("inf")
        self.best_combination = []

    def run1(self, n):
        # self.generate_prime_list(n)
        self.primenumber = generate_prime_list(n)
        self.combination = combinations(self.primenumber, 4)

        for permut in self.combination:
            iter_num = permutations(permut,2)
            # for i in range(len(permut)):
            for i in iter_num:
                a=1
                if i[0]+i[1] not in self.primenumber:
                    break
                else:
                    if sum(permut)<self.best:
                        self.best = sum(permut)
                        self.best_combination = permut

        return self



if __name__ == "__main__":
    PrimePairSum = prime_pair_sum()
    tstart = time.time()
    print((PrimePairSum.run1(n=1200)))
    tend = time.time()
    print('Run time for Q50= ', tend - tstart, 's')

