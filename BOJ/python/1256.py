# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1256
# Difficulty :    골드II
# Problem :       사전

def combination(n, r) :
    # n C r
    if r > n-r :
        r = n-r
    result = 1
    for i in range(r) :
        result *= n-i
    for i in range(r) :
        result //= i+1    
    return result

n, m, k = map(int,input().split())

if k > combination(n+m, n) :
    print("-1")
    exit()

result = ""
for i in range(n+m) :
    if n == 0 :
        result += "z"*m
        break
    if m == 0 :
        result += "a"*n
        break
    
    if k <= combination(n+m-1, m) :
        result += "a"
        n -= 1
    else :
        result += "z"
        k -= combination(n+m-1, m)
        m -= 1

print(result)