# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11725
# Difficulty :    실버II
# Problem :       트리의 부모 찾기

from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
parent = [0 for _ in range(n)]
tree = [[] for _ in range(n)]

for _ in range(n-1) :
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

queue = deque()
queue.append(0)
parent[0] = -1

while queue :
    now = queue.pop()
    for i in tree[now] :
        if parent[i] == 0 :
            parent[i] = now+1
            queue.appendleft(i)

for i in range(1, n) :
    print(f"{parent[i]}\n")