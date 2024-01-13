# 2024 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1766
# Difficulty :    골드II
# Problem :       문제집

# Minimum Spanning Tree

from queue import PriorityQueue
import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
indegree = [0 for _ in range(n)]
graph = [[] for _ in range(n)]

for _ in range(m) :
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    indegree[b] += 1
    graph[a].append(b)

queue = PriorityQueue()
for i in range(n) :
    if indegree[i] == 0 :
        queue.put(i)

while queue.qsize() > 0 :
    now = queue.get()
    print(f"{now+1} ")
    for i in graph[now] :
        indegree[i] -= 1
        if indegree[i] == 0 :
            queue.put(i)

print("\n")