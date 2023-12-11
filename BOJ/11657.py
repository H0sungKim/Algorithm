# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11657
# Difficulty :    골드IV
# Problem :       타임머신

# Bellman Ford Moore

import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
edge = []
distance = [sys.maxsize for _ in range(n)]

for _ in range(m) :
    a, b, c  = map(int, input().split())
    a -= 1
    b -= 1
    edge.append((a, b, c))

distance[0] = 0

for _ in range(n) :
    for start, end, time in edge :
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time :
            distance[end] = distance[start] + time

negativeCycle = False

for start, end, time in edge :
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time :
        negativeCycle = True

if not negativeCycle :
    for i in range(1, n) :
        if distance[i] == sys.maxsize :
            print("-1\n")
        else :
            print(f"{distance[i]}\n")
else :
    print("-1\n")