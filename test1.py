# Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>

'''
====================
Greedy
Q5. 볼링공 고르기
--------------------
문제 315p
정답 512p
====================
'''

n, m = 8,5
weight = [1, 5, 4, 3, 2, 4, 5, 2]

ball = [0] * m
for i in weight :
    ball[i-1] += 1

result = n*(n-1)//2

for i in ball :
    result -= i*(i-1)//2

print(result)