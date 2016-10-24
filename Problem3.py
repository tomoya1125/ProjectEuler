#coding: utf-8


#############################################
#	13195 の素因数は 5, 7, 13, 29 である		#
#											#
#	600851475143 の素因数のうち最大のものを求めよ	#	
#############################################


import math

def Eratosthenes(prime, x) :
	Max = int(math.sqrt(x))
	array = [0] * (Max + 1)
	#print array
	#print len(array)
	for i in range(2, len(array) + 1) :
		j = 2
		while i * j <= Max :
			array[i * j] = 1
			j = j + 1
	for i in range(2, len(array)) :
		if(array[i] == 0) :
			prime.append(i) 

prime = []

print "Input a Number!"
x = int(raw_input())
Eratosthenes(prime, x)
for i in prime :
	if(x % i == 0) :
		answer = i
print answer