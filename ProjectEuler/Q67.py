import numpy as np
import time

tstart = time.time()
triangle = np.zeros((100,100))
max_path_sum=np.zeros((100,100))

triangle_file = 'p067_triangle.txt'
with open(triangle_file, encoding='utf-8-sig') as f:
    triangle_string = f.read().splitlines()

for i in range(len(triangle_string)):
    triangle[i][0:i+1] = triangle_string[i].split(' ')

max_path_sum[99]=triangle[99]
for i in range(98,0,-1):
    for j in range(0,i+1):
        max_path_sum[i][j]=+triangle[i][j]+max(max_path_sum[i+1][j],max_path_sum[i+1][j+1])

max_path_sum[0][0]=+triangle[0][0]+max(max_path_sum[1][0],max_path_sum[1][1])
print('Answer = ',max_path_sum[0][0])
tend = time.time()
print('Run time for Q67 = ', tend - tstart, 's')
