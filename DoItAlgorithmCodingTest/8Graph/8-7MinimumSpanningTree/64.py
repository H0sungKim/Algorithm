# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1197
# Difficulty :    골드IV
# Problem :       최소 스패닝 트리

from queue import PriorityQueue
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
priorityQueue = PriorityQueue()
parent = [i for i in range(v)]

def find(num) :
    if num == parent[num] :
        return num
    else :
        parent[num] = find(parent[num])
        return parent[num]
    

for _ in range(e) :
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    priorityQueue.put((c, a, b))

useEdge = 0
result = 0

while useEdge < v-1 :
    now = priorityQueue.get()
    a = find(now[1])
    b = find(now[2])
    if a != b :
        parent[b] = a
        result += now[0]
        useEdge += 1

print(result)