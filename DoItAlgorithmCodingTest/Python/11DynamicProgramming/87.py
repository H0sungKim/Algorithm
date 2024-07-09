# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11726
# Difficulty :    실버III
# Problem :       2xn 타일링

import math

n = int(input())

num = n//2 + 1
product = 0

for i in range(num) :
    product += math.comb(n-i, i)
    product %= 10007

print(product)