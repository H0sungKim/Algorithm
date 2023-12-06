# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1747
# Difficulty :    실버I
# Problem :       소수&팰린드롬

import sys
print = sys.stdout.write

def isPalindrome(num) :
    num = str(num)
    start = 0
    end = len(num)-1

    while start <= end :
        if num[start] != num[end] :
            return False
        start += 1
        end -= 1
    return True

n = int(input())

# It is the smallest prime number and palindromic number among numbers greater than 1000000.
maxRange = 1003001

primeNum = [True for _ in range(maxRange)]
primeNum[0] = False

for i in range(2, int(maxRange**0.5)+1) :
    if primeNum[i-1] == False :
        continue
    for j in range(2, maxRange//i+1) :
        primeNum[i*j-1] = False

for i in range(n-1, maxRange) :
    if primeNum[i] :
        if isPalindrome(i+1) :

            print(f"{i+1}\n")
            exit()