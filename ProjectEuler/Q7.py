import time, numpy

from primelib.primelib import isPrime2, isPrime


tstart = time.time()
PrimeList = numpy.zeros(10001)
a=1e6
j=0

for i in range (1,int(a),1):
	if isPrime2(i)== True:
		PrimeList[j]=i
		j=j+1
		if j == 10001:
			break
			
print (PrimeList[10000])
tend = time.time()	
print('Run time for Q7 for loop =',tend-tstart,'s')


tstart = time.time()
j=0
k=0
while j<10001:
	k += 1
	if isPrime(k)==True:
		PrimeList[j]=k
		j = j+1

			
tend = time.time()
print('Run time for Q7 while loop=',tend-tstart,'s')
	
tstart = time.time()
print (isPrime(999049))	
tend = time.time()	
print('Run time for isPrime =',tend-tstart,'s')
	
tstart = time.time()
print (isPrime2(999049))	
tend = time.time()	
print ('Run time for isPrime2 =',tend-tstart,'s')