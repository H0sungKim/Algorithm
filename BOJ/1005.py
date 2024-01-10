# 2024 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1005
# Difficulty :    골드III
# Problem :       ACM Craft

# Topology Sort

from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

t = int(input())
for _ in range(t) :
    n, k = map(int, input().split())
    buildingTime = list(map(int, input().split()))
    building = [[] for _ in range(n)]
    time = [0 for _ in range(n)]
    inDegree = [0 for _ in range(n)]
    for i in range(k) :
        x, y = map(int, input().split())
        building[x-1].append(y-1)
        inDegree[y-1] += 1
    queue = deque()
    for i in range(n) :
        if inDegree[i] == 0 :
            queue.append(i)
            time[i] = buildingTime[i]
    while queue :
        now = queue.pop()
        for i in building[now] :
            time[i] = max(time[i], time[now]+buildingTime[i])
            inDegree[i] -= 1
            if inDegree[i] == 0 :
                queue.appendleft(i)

    print(f"{time[int(input())-1]}\n")