# Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>

'''
====================
Greedy
Q3. 문자열 뒤집기
--------------------
문제 313p
정답 508p
====================
'''

s = input()

oldChar = s[0]
count0 = 0
count1 = 0

for i in s :
    if i != oldChar :
        if oldChar == "0" :
            count0 += 1
        else :
            count1 += 1
    oldChar = i

if s[len(s)-1] == "0" :
    count0 += 1
else :
    count1 += 1

print(min(count0, count1))