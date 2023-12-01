# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/10986
# Difficulty :    골드III
# Problem :       나머지 합

n, m = map(int, input().split())

num = list(map(int, input().split()))

prefix = []
tempSum = 0
for i in range(n) :
    tempSum = (tempSum + num[i]) % m
    prefix.append(tempSum)

result = 0
result += prefix.count(0)

for i in list(set(prefix)) :
    temp = prefix.count(i)
    result += temp * (temp-1) // 2

print(result)