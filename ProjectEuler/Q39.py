import time
import operator

def right_tri1(n):
    a=b=c=0
    sides=[]
    for i in range(1,n):
        a=i
        remain = n-a
        for j in range(1,remain):
            b=j
            c = remain - b
            if a**2+b**2==c**2:
               sides.append([a,b,c])

    return len(sides)

def right_tri2(n):
    a=b=c=0
    sides=[]
    for i in range(1,n):
        a=i
        remain = n-a
        for j in range(1,remain):
            if b>a:
                break
            b=j
            c = remain - b
            if a**2+b**2==c**2:
               sides.append([a,b,c])

    return len(sides)

def get_most(n):
    sides = list(map(right_tri2, list(range(n))))
    max_index, max_value = max(enumerate(sides), key=operator.itemgetter(1))
    return max_index

p=1000
tstart = time.time()
# print('Ans = ',max(right_tri2(i) for i in range(p)))
print('Ans = ',get_most(p))
tend = time.time()
print('Run time for Q39 = ', tend - tstart, 's')
# tstart = time.time()
# print('Ans = ',max(right_tri1(i) for i in range(p)))
# tend = time.time()
# print('Run time for Q39 = ', tend - tstart, 's')



