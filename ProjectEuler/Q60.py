from itertools import *
import time, sys, os
import numpy as np
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
        self.prime_number_matrix = []
        self.best = float("inf")
        self.best_combination = []
        self.set=4

    def run1(self, n):#brute force appraoch
        # self.generate_prime_list(n)
        self.primenumber = generate_prime_list(n)
        self.combination = combinations(self.primenumber, self.set)

        for permut in self.combination:
            iter_num = permutations(permut,2)
            # for i in range(len(permut)):
            no = 0
            for i in iter_num:

                if int(str(i[0])+str(i[1])) not in self.primenumber:
                    no = 1
                    break

            if sum(permut)<self.best and no == 0:
                self.best = sum(permut)
                self.best_combination = permut

        return self

    def run2(self,n): #Generate look up table
        # self.generate_prime_list(n)
        self.primenumber = generate_prime_list(n)
        # self.primenumber = generate_prime_list2(n)
        self.prime_number_matrix = np.zeros((len(self.primenumber),len(self.primenumber)))
        for j in range(self.set):
            self.best_combination.append(max(self.primenumber))
        for i in range(len(self.primenumber)):
            for j in range(len(self.primenumber)):
                self.prime_number_matrix[i][j] = isPrime2(int(str(self.primenumber[i])+str(self.primenumber[j])))
                # self.prime_number_matrix[j][i] = isPrime2(self.primenumber[i] + self.primenumber[j])

        self.combination = combinations(self.primenumber, self.set)
        for permut in self.combination:
            if sum(permut)<sum(self.best_combination):
                iter_num = permutations(permut, 2)
                # for i in range(len(permut)):
                no = 0
                for i in iter_num:

                    if self.prime_number_matrix[self.primenumber.index(i[0])][self.primenumber.index(i[1])]==0:
                        no = 1
                        break

                if sum(permut) < self.best and no == 0:
                    self.best = sum(permut)
                    self.best_combination = permut


        return self

if __name__ == "__main__":
    PrimePairSum = prime_pair_sum()
    tstart = time.time()
    print((PrimePairSum.run2(n=10000)))
    tend = time.time()
    print('Run time for Q50= ', tend - tstart, 's')

