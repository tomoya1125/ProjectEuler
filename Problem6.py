# coding:utf-8

num_list = range(1, 101)
sum1 = 0
for i in num_list :
    sum1 = sum1 + i ** 2
sum2 = 0
for i in num_list :
    sum2 = sum2 + i
sum2 = sum2 ** 2
print sum2 - sum1