#coding-utf-8

import math

def Eratosthenes(x) :
    Max = int(math.sqrt(x))
    array = [0] * (x + 1)
    #print array
   # print len(array)
    prime = []
    for i in range(2, Max + 1) :
        j = 2
        while i * j < len(array) :
            #print i*j
            array[i * j ] = 1
            j = j + 1
    for i in range(2, len(array)) :
        if(array[i] == 0) :
            prime.append(i)

    return prime

def main() :
    prime = []
    i = 1000000000
    while len(prime) < 10002 :
        prime = Eratosthenes(i)
        i = i * 10
    print prime[10000]

if __name__ == '__main__':
    main()