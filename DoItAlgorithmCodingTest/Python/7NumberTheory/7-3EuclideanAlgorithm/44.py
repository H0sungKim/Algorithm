# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1033
# Difficulty :    골드II
# Problem :       칵테일

def getGCD(num1, num2) :
    while num2 :
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1

n = int(input())
ingredient = [[] for _ in range(n)]
rate = [0 for _ in range(n)]
lcm = 1

for _ in range(n-1) :
    a, b, p, q = map(int, input().split())
    gcd = getGCD(p, q)
    p //= gcd
    q //= gcd
    ingredient[a].append((b, p, q))
    ingredient[b].append((a, q, p))
    lcm *= p*q

def DFS(index) :
    for i in ingredient[index] :
        next = i[0]
        if rate[next] == 0 :
            rate[next] = rate[index] * i[2] // i[1]
            DFS(next)

rate[0] = lcm
DFS(0)

temp = rate[0]

for i in range(1, n) :
    temp = getGCD(temp, rate[i])

for i in range(n) :
    print(rate[i]//temp, end=" ")