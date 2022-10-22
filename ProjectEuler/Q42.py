import numpy as np
from seq_toolbox import *

def triangle_number_list(n):
    sequence=[]
    for i in range(1,n):
        sequence.append( i*(i+1)/2)
    return sequence

with open('./ProjectEuler/Q42_words.txt') as f:
    content = f.readlines()

for line in content:
    full_line = line.split(',')

word = np.array([])
for i in range(len(full_line)):
    word = np.append(word, full_line[i].replace('"', ''))

# Compute sum from letters
sum = np.array([])
for i in range(len(word)):
    line_sum = 0
    for j in range(len(word[i])):
        line_sum += ord(word[i][j]) - 64
    sum = np.append(sum, line_sum)

# Generate triangle number list
tri_seq = triangle_number_list(40)

# Check if sum is in the triangle number list
count = 0
for k in range(len(sum)):
    if sum[k] in tri_seq:
        count += 1
# number = ord(character) - 64
print('Answer for Q42 =', count)
