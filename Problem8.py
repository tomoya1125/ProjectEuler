#coding:utf-8

line = raw_input()
num = map(int, line)
i = 0
end = 13
MAX = 0
while i + end < len(num) :
    tmp = 1
    for j in xrange(i, i + end) :
        tmp = tmp * num[j]
    if MAX < tmp :
        MAX = tmp
    i = i + 1
print MAX