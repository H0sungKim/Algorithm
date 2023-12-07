# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1456
# Difficulty :    골드V
# Problem :       거의 소수

# Sieve of Eratosthenes

a, b = map(int, input().split())
sqrtB = int(b**0.5)

primeNumList = [True for _ in range(sqrtB)]
primeNumList[0] = False

for i in range(2, int(sqrtB**0.5)+1) :
    if primeNumList[i-1] == False :
        continue
    for j in range(2, sqrtB//i+1) :
        primeNumList[i*j-1] = False

result = 0
for i in range(1, sqrtB) :
    if primeNumList[i] :
        # print(f"{i+1}\n")
        primeNum = i+1
        temp = primeNum * primeNum
        while temp <= b :
            if temp >= a :
                # print(temp)
                result += 1
            temp *= primeNum

print(result)