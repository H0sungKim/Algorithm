# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2023
# Difficulty :    골드V
# Problem :       신기한 소수

# DFS

# The first digit must be one of 2,3,5,7 and the remaining digits must be one of 1,3,7,9.

import sys
print = sys.stdout.write

n = int(input())

def isPrime(num) :
    for i in range(2, int(num**0.5)+1) :
        if num % i == 0 :
            return False
    return True

def findPrimeNumDFS(num, depth) :
    if depth == 1 :
        print(f"{num}\n")
        return
    depth -= 1
    num *= 10
    if isPrime(num+1) :
        findPrimeNumDFS(num+1, depth)
    if isPrime(num+3) :
        findPrimeNumDFS(num+3, depth)
    if isPrime(num+7) :
        findPrimeNumDFS(num+7, depth)
    if isPrime(num+9) :
        findPrimeNumDFS(num+9, depth)
    
findPrimeNumDFS(2, n)
findPrimeNumDFS(3, n)
findPrimeNumDFS(5, n)
findPrimeNumDFS(7, n)