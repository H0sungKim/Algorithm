# 2022 Hosung.Kim <hyongak516@mail.hongik.ac.kr>

'''
====================
Greedy
Q4. 만들 수 없는 금액
--------------------
문제 314p
정답 509p
====================
'''

n = int(input())
coin = sorted(list(map(int, input().split())))

minCon = 1
for i in coin :
    if minCon < i :
        break
    minCon += i

print(minCon)