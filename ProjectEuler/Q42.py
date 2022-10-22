import time
from pathlib import Path

def triangle_number_list(n):
    sequence=[]
    for i in range(1,n):
        sequence.append( i*(i+1)/2)
    return sequence

tstart = time.time()

with open(Path.cwd() / 'ProjectEuler' / 'Q42_words.txt') as f:
    words = [word.replace('"','') for word in f.readlines()[0].split(',')]

# Compute sum from letters
sum_array = [sum([ord(letter)-64 for letter in word]) for word in words]

# Check if sum is in the triangle number list
count = sum(1 for line_sum in sum_array if line_sum in triangle_number_list(40))
print('Answer for Q42 =', count)
tend = time.time()
print('Run time for Q42 = ', tend - tstart, 's')