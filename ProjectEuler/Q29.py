from itertools import *
# n=6
n=101
# Generate a and b as list
a = list(range(2,n))
b = list(range(2,n))

combination = list(permutations(a+b, 2))
number_from_combination = [comb[0]**comb[1] for comb in combination ]

distinct_numbers = set(number_from_combination)
print('Answer of Q29 = ',len(distinct_numbers))
