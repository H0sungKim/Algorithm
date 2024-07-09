# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1325
# Difficulty :    실버I
# Problem :       효율적인 해킹

from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())

trust = [[] for _ in range(n)]
count = [0 for _ in range(n)]

for _ in range(m) :
    a, b = map(int, input().split())
    trust[a-1].append(b-1)

def BFS(index) :
    queue = deque()
    queue.append(index-1)
    visited[index-1] += 1
    while queue :
        nowNode = queue.pop()
        for i in trust[nowNode] :
            if not visited[i] :
                visited[i] = True
                queue.appendleft(i)
                count[i] += 1

for i in range(n) :
    visited = [False for _ in range(n)]
    BFS(i)

maxCount = max(count)
for i in range(n) :
    if count[i] == maxCount :
        print(f"{i+1} ")