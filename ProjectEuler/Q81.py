import numpy as np
import time

from pathlib import Path

tstart = time.time()
matrix = np.zeros((80,80))
dumpy_matrix = np.zeros((5,5))
grid = np.zeros((5,5))
matrix_file = Path.cwd() / 'ProjectEuler' / 'matrix.txt'
with open(matrix_file) as f:
    matrix_string = f.read().splitlines()

for i in range(len(matrix_string)):
    matrix[i] = matrix_string[i].split(',')

# Dummy matrix example
# See https://www.youtube.com/watch?v=lBRtnuxg-gU
# dumpy_matrix = np.zeros((5,5))
# dumpy_matrix[0]=[131,673,234,102,18]
# dumpy_matrix[1]=[201,96,342,965,150]
# dumpy_matrix[2]=[630,803,746,422,111]
# dumpy_matrix[3]=[537,699,497,121,956]
# dumpy_matrix[4]=[805,732,524,37,331]
#
# for i in range(len(dumpy_matrix) - 2, -1, -1):
#     dumpy_matrix[len(dumpy_matrix) - 1][i] += dumpy_matrix[len(dumpy_matrix) - 1][i + 1]
#     dumpy_matrix[i][len(dumpy_matrix) - 1] += dumpy_matrix[i + 1][len(dumpy_matrix) - 1]
#
# for i in range(len(dumpy_matrix) - 2, -1, -1):
#     for j in range(len(dumpy_matrix) - 2, -1, -1):
#         dumpy_matrix[i][j] += min(dumpy_matrix[i + 1][j],dumpy_matrix[i][j+1])


for i in range(len(matrix) - 2, -1, -1):
    matrix[len(matrix) - 1][i] += matrix[len(matrix) - 1][i + 1]
    matrix[i][len(matrix) - 1] += matrix[i + 1][len(matrix) - 1]

for i in range(len(matrix) - 2, -1, -1):
    for j in range(len(matrix) - 2, -1, -1):
        matrix[i][j] += min(matrix[i + 1][j],matrix[i][j+1])


print('Answer = ',matrix[0][0])
tend = time.time()
print('Run time for Q81 = ', tend - tstart, 's')