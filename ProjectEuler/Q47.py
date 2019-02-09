import time, numpy, sys, os

ThisFolder = os.path.dirname(os.path.abspath(__file__))
PathsToAdd = [os.path.abspath(ThisFolder),
              os.path.abspath(os.path.join(ThisFolder,'..'))]

for PathToAdd in PathsToAdd:
    if PathToAdd not in sys.path:
        sys.path.insert(0,PathToAdd)

from PrimeLib import *

limit = 150000
first_consec_number = []
distinct_prime_number_number = 4
for i in range(600,limit,1):

    unique_list1 = list(set(chekc_unique_prime_factor(factorisePrime(i))))
    unique_list2 = list(set(chekc_unique_prime_factor(factorisePrime(i+1))))
    unique_list3 = list(set(chekc_unique_prime_factor(factorisePrime(i+2))))
    unique_list4 = list(set(chekc_unique_prime_factor(factorisePrime(i+3))))

    all_factor = unique_list1 + unique_list2 + unique_list3 + unique_list4

    set_all_factor = set(all_factor)

    if len(set_all_factor) == len(all_factor) and len(unique_list1)==len(unique_list2)==len(unique_list3)==len(unique_list4) == distinct_prime_number_number:
        first_consec_number.append(i)

print (first_consec_number)