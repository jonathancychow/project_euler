import numpy as np
import time

tstart = time.time()
input_tri=np.zeros((15,15))
max_path_sum=np.zeros((15,15))

input_tri[0][0]=75
input_tri[1][0:2]=[95,64]
input_tri[2][0:3]=[17,47,82]
input_tri[3][0:4]=[18,35,87,10]
input_tri[4][0:5]=[20,4,82,47,65]
input_tri[5][0:6]=[19,1,23,75,3,34]
input_tri[6][0:7]=[88,2,77,73,7,63,67]
input_tri[7][0:8]=[99,65,4,28,6,16,70,92]
input_tri[8][0:9]=[41,41,26,56,83,40,80,70,33]
input_tri[9][0:10]=[41,48,72,33,47,32,37,16,94,29]
input_tri[10][0:11]=[53,71,44,65,25,43,91,52,97,51,14]
input_tri[11][0:12]=[70,11,33,28,77,73,17,78,39,68,17,57]
input_tri[12][0:13]=[91,71,52,38,17,14,91,43,58,50,27,29,48]
input_tri[13][0:14]=[63,66,4,68,89,53,67,30,73,16,69,87,40,31]
input_tri[14][0:15]=[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

max_path_sum[14]=input_tri[14]
for i in range(13,0,-1):
    # max_path_sum[i][0]=max_path_sum[i+1][0]+input_tri[i][0]
    for j in range(0,i+1):
        max_path_sum[i][j]=+input_tri[i][j]+max(max_path_sum[i+1][j],max_path_sum[i+1][j+1])


max_path_sum[0][0]=+input_tri[0][0]+max(max_path_sum[1][0],max_path_sum[1][1])
# answer = max_path_sum
print('Answer = ',max_path_sum[0][0])
tend = time.time()
print('Run time for Q18 = ', tend - tstart, 's')
