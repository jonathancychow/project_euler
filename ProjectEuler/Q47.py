import time

from primelib.primelib import chekcUniquePrimeFactor, factorisePrime


# set the upper limit
limit = 150000
tstart = time.time()

first_consec_number = []
distinct_prime_factor_number = 4
for i in range(10,limit,1):

    # factorisePrime return a list of prime factors. chekcUniquePrimeFactor turns the list to unique prime factor
    # ie (2,2,2,3,3,5) to (8,9,5)
    # set returns a unqiue list
    unique_list1 = list(set(chekcUniquePrimeFactor(factorisePrime(i))))
    unique_list2 = list(set(chekcUniquePrimeFactor(factorisePrime(i+1))))
    unique_list3 = list(set(chekcUniquePrimeFactor(factorisePrime(i+2))))
    unique_list4 = list(set(chekcUniquePrimeFactor(factorisePrime(i+3))))

    all_factor = unique_list1 + unique_list2 + unique_list3 + unique_list4

    set_all_factor = set(all_factor)

    if len(set_all_factor) == len(all_factor) and len(unique_list1)==len(unique_list2)==len(unique_list3)==len(unique_list4) == distinct_prime_factor_number:
        first_consec_number.append(i)

print (first_consec_number)
tend = time.time()
print('Run time for Q47= ',tend-tstart,'s')