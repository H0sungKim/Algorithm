# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1753
# Difficulty :    골드IV
# Problem :       최단경로

from queue import PriorityQueue
import sys
input = sys.stdin.readline
print = sys.stdout.write

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v)]
distance = [sys.maxsize for _ in range(v)]
visited = [False for _ in range(v)]

for _ in range(e) :
    a, b, w = map(int, input().split())
    graph[a-1].append((b-1, w))

queue = PriorityQueue()
queue.put((0, k-1))
distance[k-1] = 0

while queue.qsize() > 0 :
    now = queue.get()
    if visited[now[1]] :
        continue
    visited[now[1]] = True
    for i in graph[now[1]] :
        if distance[i[0]] > i[1] + distance[now[1]] :
            distance[i[0]] = i[1] + distance[now[1]]
            queue.put((distance[i[0]], i[0]))
            
for i in range(v) :
    if visited[i] :
        print(f"{distance[i]}\n")
    else :
        print("INF\n")