# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1976
# Difficulty :    골드IV
# Problem :       여행 가자

# Union Find Algorithm

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
city = []

for _ in range(n) :
    city.append(list(map(int, input().split())))

travel = list(map(int, input().split()))

parent = [i for i in range(n)]

def find(a) :
    if a == parent[a] :
        return a
    else :
        parent[a] = find(parent[a])
        return parent[a]
    
for i in range(n) :
    for j in range(n) :
        if city[i][j] == 1 :
            parent[find(i)] = find(j)

index = find(travel[0]-1)

for i in travel :
    if index != find(i-1) :
        print("NO")
        exit()

print("YES")