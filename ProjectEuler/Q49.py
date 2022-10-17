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

class PrimePermutations:

    def __init__(self):
        self.combination = []
        self.digit = 4
        self.answer = set()

    def run1(self): #brute force appraoch

        self.combination = combinations_with_replacement(list(range(1,10)), self.digit)
        for combination in self.combination:
            found = False
            for permutation_digit in permutations(combination):
                prime_list = list({int(''.join([str(this)for this in this_num ])) for this_num in permutations(permutation_digit) \
                    if isPrime2(int(''.join([str(this)for this in this_num])))})
                
                # Only carry on if there are 3 values or more in this list
                if len(prime_list) >= 3:
                    difference_map = defaultdict(list) 
                    for prim_list_combination in combinations(prime_list,2):
                        difference = abs(prim_list_combination[0] - prim_list_combination[1])
                        difference_map[difference].append((prim_list_combination[0], prim_list_combination[1]))
                    
                    difference_list_with_2_or_more = [difference for difference, prime_num_pair in difference_map.items() if len(prime_num_pair)>=2]
                    for difference in difference_list_with_2_or_more:
                        # flatten difference map
                        difference_set = {prim for difference_tuple in difference_map[difference] for prim in difference_tuple}

                        if len(difference_set)<4:
                            self.answer.add(tuple(sorted(difference_set)))
                            found = True
                            break
                
                if found:
                    break


if __name__ == "__main__":
    prime_permutations = PrimePermutations()
    tstart = time.time()
    prime_permutations.run1()
    print('Combination = ',prime_permutations.answer)
    tend = time.time()
    print('Run time for Q49 = ', tend - tstart, 's')

