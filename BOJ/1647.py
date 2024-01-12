# 2024 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1647
# Difficulty :    골드IV
# Problem :       도시 분할 계획

# Minimum Spanning Tree

from queue import PriorityQueue
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
priorityQueue = PriorityQueue()

for _ in range(m) :
    a, b, c = map(int, input().split())
    priorityQueue.put((c, a-1, b-1))

usedEdge = 0
result = 0
parent = [i for i in range(n)]

def find(num) :
    if num == parent[num] :
        return num
    else :
        parent[num] = find(parent[num])
        return parent[num]

while usedEdge < n-2 :            
    now = priorityQueue.get()
    a = find(now[1])
    b = find(now[2])
    if a != b :
        parent[b] = a
        result += now[0]
        usedEdge += 1

print(result)