# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2436
# Difficulty :    골드V
# Problem :       공약수

# Euclidean Algorithm

import math

def getGCD(num1, num2) :
    while num2 :
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1

gcd, lcm = map(int, input().split())

divisor = []

for i in range(1, math.ceil(math.sqrt(lcm))+1) :
    if lcm%i == 0 :
        if i>=gcd :
            divisor.append(i)
        if lcm//i>=gcd :
            divisor.append(lcm//i)

divisor.sort()

minSum = 200000000

for i in range(len(divisor)-1) :
    for j in range(i+1, len(divisor)) :
        if getGCD(divisor[i], divisor[j]) == gcd and divisor[i] + divisor[j] <= minSum :
            resultNum1 = divisor[i]
            resultNum2 = divisor[j]

print(resultNum1, resultNum2)