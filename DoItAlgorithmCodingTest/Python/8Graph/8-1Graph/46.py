# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/18352
# Difficulty :    실버II
# Problem :       특정 거리의 도시 찾기

from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

road = [[] for _ in range(n)]
visited = [-1 for _ in range(n)]

for _ in range(m) :
    a, b = map(int, input().split())
    road[a-1].append(b-1)

# BFS
queue = deque()
queue.append(x-1)
visited[x-1] += 1
while queue :
    nowNode = queue.pop()
    for i in road[nowNode] :
        if visited[i] < 0 :
            visited[i] = visited[nowNode] + 1
            queue.appendleft(i)

flag = 0
for i in range(n) :
    if visited[i] == k :
        print(i+1)
        flag += 1

if flag == 0 :
    print("-1")