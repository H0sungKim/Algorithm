# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1929
# Difficulty :    실버III
# Problem :       소수 구하기

import sys
print = sys.stdout.write

m, n = map(int, input().split())

primeNum = [True for _ in range(n)]
primeNum[0] = False

for i in range(2, int(n**0.5)+1) :
    if primeNum[i-1] == False :
        continue
    for j in range(2, n//i+1) :
        primeNum[i*j-1] = False

for i in range(m-1, n) :
    if primeNum[i] :
        print(f"{i+1}\n")