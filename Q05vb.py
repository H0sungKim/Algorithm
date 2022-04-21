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

n, m = map(int, input().split())
weight = list(map(int, input().split()))

ball = [0] * m
for i in weight :
    ball[i-1] += 1

result = 0

for i in ball :
    n -= i
    result += n * i

print(result)