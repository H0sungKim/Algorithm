# 2022 Hosung.Kim <hyongak516@mail.hongik.ac.kr>

'''
====================
Greedy
Q2. 곱하기 혹은 더하기
--------------------
문제 312p
정답 507p
====================
'''

s = input()

num = 0
for i in s :
    i = int(i)
    if i<=1 or num<=1 :
        num += i
    else :
        num *= i

print(num)