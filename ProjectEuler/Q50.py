from itertools import *
import time, sys, os
ThisFolder = os.path.dirname(os.path.abspath(__file__))
PathsToAdd = [os.path.abspath(ThisFolder),
              os.path.abspath(os.path.join(ThisFolder,'..'))]
for PathToAdd in PathsToAdd:
    if PathToAdd not in sys.path:
        sys.path.insert(0,PathToAdd)
from PrimeLib import *



class consec_prime_sum:

    def __init__(self):
        self.number =[]
        # self.number.append(2)
        self.primenumber = []
        self.sequence = []
        self.sequence_sum = []

    def run(self, n):
        # self.generate_prime_list(n)
        self.primenumber = generate_prime_list(n)
        sequence = 0
        for i in range(0,len(self.primenumber)-1):
            # for j in range(len(self.primenumber[i])):
            start = i
            self.addsequence =[] #temp sequence, only add to sequence if the number is prime
            self.sequence.append([])
            self.number.append([])
            self.sequence_sum = self.primenumber[start] + self.primenumber[start+1]
            self.addsequence.append(self.primenumber[start])

            # if self.sequence_sum in self.primenumber:
            #     self.sequence[i-1].append(self.primenumber[start-1])
                # self.sequence[i-1].append(self.primenumber[start])
            while self.sequence_sum < n:
                # self.sequence[i - 1].append(self.primenumber[start])
                self.addsequence.append(self.primenumber[start+1])
                if self.sequence_sum in self.primenumber:
                    # self.sequence_sum not in self.number:
                    # self.number[i-1].append(self.sequence_sum)
                    self.number[i]=self.sequence_sum
                    self.sequence[i]=self.sequence[i] + self.addsequence
                    self.addsequence=[]

                start += 1
                self.sequence_sum += self.primenumber[start+1]

        dim=[]
        for i in range(len(self.sequence)):
            dim.append(len(self.sequence[i]))
        max_sequence_index = dim.index(max(dim))

        return self.number[max_sequence_index]


if __name__ == "__main__":
    ConsecPrimeSum = consec_prime_sum()
    tstart = time.time()
    print((ConsecPrimeSum.run(n=1000000)))
    tend = time.time()
    print('Run time for Q50= ', tend - tstart, 's')

