# 2024 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/4386
# Difficulty :    골드III
# Problem :       별자리 만들기

# Minimum Spanning Tree

from queue import PriorityQueue
import math
import sys
input = sys.stdin.readline

n = int(input())
stars = []
priorityQueue = PriorityQueue()

for _ in range(n) :
    stars.append(tuple(map(float, input().split())))

for i in range(n-1) :
    for j in range(i, n) :
        distance = math.sqrt(math.pow(stars[i][0]-stars[j][0], 2) + math.pow(stars[i][1]-stars[j][1], 2))
        priorityQueue.put((distance, i, j))

useEdge = 0
result = 0
parent = [i for i in range(n)]

def find(num) :
    if num == parent[num] :
        return num
    else :
        parent[num] = find(parent[num])
        return parent[num]

while useEdge < n-1 :
    now = priorityQueue.get()
    a = find(now[1])
    b = find(now[2])
    if a != b :
        parent[b] = a
        result += now[0]
        useEdge += 1

print(result)