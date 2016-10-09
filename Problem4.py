#!/usr/bin/python
# coding: utf-8

def CheckPNum(num) :
    x = []
    for i in reversed(xrange(Digits(num)+1)) :
        digit = PickDigitNum(num, i)
        num = num - digit * (10 ** i)
        x.append(digit)
    if x == x[::-1] :
        return True

    return False

def Digits(num) :
    digit = 0
    x = 10
    while num / x != 0 :
        digit = digit + 1
        x = x * 10

    return digit

def PickDigitNum(num, digit) :
    return num / 10 ** digit

if __name__ == '__main__' :
    num = []
    for i in range(100, 1000) :
        for j in range(100, 1000) :
            num.append(i * j)

    for i in sorted(num, reverse=True) :
        if CheckPNum(i) == True :
            print i
            break
