# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1707
# Difficulty :    골드IV
# Problem :       이분 그래프

from collections import deque
import sys
input = sys.stdin.readline

k = int(input())

for _ in range(k) :

    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]
    visited = [-1 for _ in range(v)]
    for _ in range(e) :
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    flag = False

    for i in range(v) :
        if flag :
            break
        if visited[i] >= 0 :
            continue
        queue = deque()
        queue.append(i)
        visited[i] = 0
        
        while queue :
            if flag :
                break
            nowNode = queue.pop()
            for j in graph[nowNode] :
                if visited[j] < 0 :
                    visited[j] = (visited[nowNode]+1) % 2
                    queue.appendleft(j)
                else :
                    if visited[j] == visited[nowNode] :
                        print("NO")
                        flag = True
                        break
    if not flag :
        print("YES")