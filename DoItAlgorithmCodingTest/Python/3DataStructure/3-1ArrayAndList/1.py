# 2021 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11720
# Difficulty :    브론즈IV
# Problem :       숫자의 합

n = int(input())
numList = input()
numSum = 0

for i in range(n) :
    numSum += int(numList[i])

print(numSum)