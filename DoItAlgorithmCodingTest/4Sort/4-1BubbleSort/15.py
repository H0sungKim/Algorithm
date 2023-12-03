# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2750
# Difficulty :    브론즈I
# Problem :       수 정렬하기 1

n = int(input())
num = []

for i in range(n) :
    num.append(int(input()))

for i in range(n-1) :
    for j in range(n-1-i) :
        if num[j] > num[j+1] :
            temp = num[j]
            num[j] = num[j+1]
            num[j+1] = temp

for i in num :
    print(i)