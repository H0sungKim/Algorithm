# 2024 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/9527
# Difficulty :    골드II
# Problem :       1의 개수 세기

import math

a, b = map(int, input().split())

length = math.floor(math.log2(b))+1
dp = [0]
for i in range(length-1) :
    dp.append(2**i + 2*dp[len(dp)-1])

def getOneSum(num) :
    result = 0
    oneCount = 0
    for i in range(length) :
        if num >= 1 << length-i-1 :
            result += dp[len(dp)-i-1] + oneCount * 2**(length-i-1)
            num -= 1 << length-i-1
            oneCount += 1
            
    result += oneCount
    return result

result = getOneSum(b) - getOneSum(a)

for i in range(length) :
    if a & 1 << i != 0 :
        result += 1

print(result)