# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/13398
# Difficulty :    골드V
# Problem :       연속합 2

n = int(input())

num = list(map(int, input().split()))
leftPrefix = [num[0]]
rightPrefix = [num[-1]]

for i in range(n-1) :
    if leftPrefix[i] > 0 :
        leftPrefix.append(leftPrefix[i] + num[i+1])
    else :
        leftPrefix.append(num[i+1])

for i in range(n-1) :
    if rightPrefix[i] > 0 :
        rightPrefix.append(rightPrefix[i] + num[n-2-i])
    else :
        rightPrefix.append(num[n-2-i])
rightPrefix = rightPrefix[::-1]

maxNum = max(num)
for i in range(1, n-1) :
    maxNum = max(maxNum, leftPrefix[i-1] + rightPrefix[i+1])

maxNum = max(maxNum, max(leftPrefix), max(rightPrefix))

print(maxNum)