# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/10844
# Difficulty :    실버I
# Problem :       쉬운 계단 수

n = int(input())

num = [1 for _ in range(10)]
num[0] = 0

for _ in range(n-1) :
    temp = [0 for _ in range(10)]
    for j in range(10) :
        if j-1 >= 0 :
            temp[j] += num[j-1]
        if j+1 <= 9 :
            temp[j] += num[j+1]
        temp[j] %= 1000000000
    num = temp[:]

print(sum(num)%1000000000)