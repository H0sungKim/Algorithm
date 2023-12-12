# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/17472
# Difficulty :    골드I
# Problem :       다리 만들기 2

# BFS, Minimum Spanning Tree

from queue import PriorityQueue
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
priorityQueue = PriorityQueue()
islandMap = []

for _ in range(n) :
    islandMap.append(list(map(int, input().split())))

# Create an islandMap.
queue = deque()
islandCount = 0
for i in range(n) :
    for j in range(m) :
        if islandMap[i][j] == 1 :
            queue.append((i, j))
            while queue :
                now = queue.pop()
                islandMap[now[0]][now[1]] = islandCount * 10 + 10
                if now[0]-1 >= 0 :
                    if islandMap[now[0]-1][now[1]] == 1 :
                        islandMap[now[0]-1][now[1]] = islandCount * 10 + 10
                        queue.append((now[0]-1, now[1]))
                if now[0]+1 < n :
                    if islandMap[now[0]+1][now[1]] == 1 :
                        islandMap[now[0]+1][now[1]] = islandCount * 10 + 10
                        queue.append((now[0]+1, now[1]))
                if now[1]-1 >= 0 :
                    if islandMap[now[0]][now[1]-1] == 1 :
                        islandMap[now[0]][now[1]-1] = islandCount * 10 + 10
                        queue.append((now[0], now[1]-1))
                if now[1]+1 < m :
                    if islandMap[now[0]][now[1]+1] == 1 :
                        islandMap[now[0]][now[1]+1] = islandCount * 10 + 10
                        queue.append((now[0], now[1]+1))
            islandCount += 1

# Get all bridge cases.
bridge = PriorityQueue()

for i in range(n) :
    for j in range(m) :
        if i == 3 :
            pass
        if islandMap[i][j] == 0 :
            continue
        for k in range(i) :
            if islandMap[i-1-k][j] != 0 :
                if islandMap[i-1-k][j] != islandMap[i][j] :
                    if k > 1 :
                        bridge.put((k, islandMap[i][j]//10-1, islandMap[i-1-k][j]//10-1))
                break
        for k in range(n-i-1) :
            if islandMap[i+1+k][j] != 0 :
                if islandMap[i+1+k][j] != islandMap[i][j] :
                    if k > 1 :
                        bridge.put((k, islandMap[i][j]//10-1, islandMap[i+1+k][j]//10-1))
                break
        for k in range(j) :
            if islandMap[i][j-1-k] != 0 :
                if islandMap[i][j-1-k] != islandMap[i][j] :
                    if k > 1 :
                        bridge.put((k, islandMap[i][j]//10-1, islandMap[i][j-1-k]//10-1))
                break
        for k in range(m-j-1) :
            if islandMap[i][j+1+k] != 0 :
                if islandMap[i][j+1+k] != islandMap[i][j] :
                    if k > 1 :
                        bridge.put((k, islandMap[i][j]//10-1, islandMap[i][j+1+k]//10-1))
                break
                
def find(num) :
    if num == parent[num] :
        return num
    else :
        parent[num] = find(parent[num])
        return parent[num]

useEdge = 0
result = 0
parent = [i for i in range(islandCount)]

while bridge.qsize() > 0 :
    now = bridge.get()
    a = find(now[1])
    b = find(now[2])
    if a != b :
        parent[b] = a
        result += now[0]
        useEdge += 1

if useEdge == islandCount-1 :
    print(result)
else :
    print("-1")