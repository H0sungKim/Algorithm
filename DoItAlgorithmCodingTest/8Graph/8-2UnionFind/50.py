# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1717
# Difficulty :    골드V
# Problem :       집합의 표현

# Union Find Algorithm

from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(a) :
    if a == parent[a] :
        return a
    else :
        parent[a] = find(parent[a])
        return parent[a]

for _ in range(m) :
    command, a, b = map(int, input().split())
    if command == 0 :
        parent[find(a)] = find(b)
    elif command == 1 :
        if find(a) == find(b) :
            print("YES\n")
        else :
            print("NO\n")