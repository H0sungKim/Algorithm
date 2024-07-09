# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2252
# Difficulty :    골드III
# Problem :       줄 세우기

from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
indegree = [0 for _ in range(n)]
graph = [[] for _ in range(n)]

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    indegree[b-1] += 1

queue = deque()

for i in range(n) :
    if indegree[i] == 0 :
        queue.append(i)

while queue :
    now = queue.pop()
    print(f"{now+1} ")
    for i in graph[now] :
        indegree[i] -= 1
        if indegree[i] == 0 :
            queue.appendleft(i)