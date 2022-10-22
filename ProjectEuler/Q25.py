import numpy as np

def fibonacci (n):
    # numpy doesnt work, uint 64 does not even have 1000 digit
    # sequence = np.array([1],dtype=np.float64)
    # sequence = np.append(sequence,1)
    sequence = [1,1]

    for i in range(2,n,1):
        # sequence = np.append(sequence, sequence[i-1]+sequence[i-2])
        sequence.append(sequence[i-1]+sequence[i-2])


    return sequence[n-1]

i=1
while len(str(fibonacci(i)))<1000:
    i +=1

print('Answer = ',i)
# print(i)
# print(fibonacci(4782))
