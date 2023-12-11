# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1219
# Difficulty :    플래티넘V
# Problem :       오민식의 고민

# Bellman Ford Moore

import sys
input = sys.stdin.readline

n, a, b, m = map(int, input().split())
edge = []
distance = [-sys.maxsize for _ in range(n)]

for _ in range(m) :
    start, end, price = map(int, input().split())
    edge.append((start, end, price))

city = list(map(int, input().split()))

distance[a] = city[a]

for i in range(n*3) :
    for start, end, price in edge :
        if distance[start] == -sys.maxsize :
            continue
        if distance[start] == sys.maxsize :
            distance[end] = sys.maxsize
        elif distance[end] < distance[start] - price + city[end] :
            if i >= n :
                distance[end] = sys.maxsize
            else :
                distance[end] = distance[start] - price + city[end]

if distance[b] == -sys.maxsize :
    print("gg")
elif distance[b] == sys.maxsize :
    print("Gee")
else :
    print(distance[b])