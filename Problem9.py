#coding:utf-8

def Compare(a, b, c) :
    return a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2

for a in xrange(1, 498) :
    for b in xrange(1, 499) :
        for c in xrange(1, 500) :
            if Compare(a, b, c) == True :
                print a,b,c
                print a*b*c
                exit(0)
                exit(0)
# test
