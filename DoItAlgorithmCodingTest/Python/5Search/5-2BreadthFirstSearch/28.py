# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1167
# Difficulty :    골드II
# Problem :       트리의 지름

from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
nord = [[] for _ in range(v)]
visited = [False for _ in range(v)]
distance = [0 for _ in range(v)]
for _ in range(v) :
    data = list(map(int, input().split()))
    for i in range((len(data)-2)//2) :
        nord[data[0]-1].append((data[2*i+1]-1, data[2*i+2]))

def BFS(index) :
    queue = deque()
    queue.append(index)
    visited[index] = True
    while queue :
        nowNode = queue.pop()
        for i in nord[nowNode] :
            if not visited[i[0]] :
                visited[i[0]] = True
                queue.appendleft(i[0])
                distance[i[0]] = distance[nowNode] + i[1]

BFS(0)
maxNord = distance.index(max(distance))
visited = [False for _ in range(v)]
distance = [0 for _ in range(v)]

BFS(maxNord)
print(max(distance))