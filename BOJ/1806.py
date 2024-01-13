# 2024 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1806
# Difficulty :    골드IV
# Problem :       부분합

# Prefix Sum, Two Pointer

import sys
input = sys.stdin.readline

n, s = map(int, input().split())

num = list(map(int, input().split()))
tempSum = 0
prefixSum = [0]
for i in num :
    tempSum += i
    prefixSum.append(tempSum)

start = 0
end = 0
minLength = 999999

while end <= n and start <= n :
    subtotal = prefixSum[end] - prefixSum[start]
    if subtotal < s :
        end += 1
    else :
        minLength = min(minLength, end-start)
        start += 1
        
if minLength == 999999 :
    minLength = 0
print(minLength)