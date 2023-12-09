# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1854
# Difficulty :    플래티넘V
# Problem :       K번째 최단경로 찾기

import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m, k = map(int, input().split())

city = [[] for _ in range(n)]
time = [[sys.maxsize for _ in range(k)] for _ in range(n)]

for _ in range(m) :
    a, b, c = map(int, input().split())
    city[a-1].append((c, b-1))

time[0][0] = 0
queue = [(0, 0)]
while queue :
    now = heapq.heappop(queue)
    for i in city[now[1]] :
        if time[i[1]][k-1] > now[0] + i[0] :
            time[i[1]][k-1] = now[0] + i[0]
            time[i[1]].sort()
            heapq.heappush(queue, (now[0] + i[0], i[1]))

for i in range(n) :
    if time[i][k-1] == sys.maxsize :
        print("-1\n")
    else :
        print(f"{time[i][k-1]}\n")