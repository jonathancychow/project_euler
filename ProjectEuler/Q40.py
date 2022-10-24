import time
import math
tstart = time.time()
num_string = ''.join([str(i) for i in range(0,1000000)])
answer = map(int,[num_string[1],num_string[10],num_string[100],num_string[1000],num_string[10000],num_string[100000],num_string[1000000]])
print('Answer = ',math.prod(answer))
tend = time.time()
print('Run time for Q40= ',tend-tstart,'s')
