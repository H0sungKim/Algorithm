# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/14501
# Difficulty :    실버III
# Problem :       퇴사

n = int(input())
price = [0 for _ in range(n+1)]

for i in range(n) :
    t, p = map(int, input().split())
    if i+t > n :
        continue
    for j in range(i+t, n+1) :
        price[j] = max(price[i]+p, price[j])
    
print(price[n])