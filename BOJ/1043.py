# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1043
# Difficulty :    골드IV
# Problem :       거짓말

# Union Find Algorithm

import sys
input = sys.stdin.readline

def find(a) :
    if a == parent[a] :
        return a
    else :
        parent[a] = find(parent[a])
        return parent[a]

n, m = map(int, input().split())
truth = list(map(int, input().split()))
party = []
parent = [i for i in range(n)]

for _ in range(m) :
    temp = list(map(int, input().split()))
    first = find(temp[1]-1)
    for i in range(temp.pop(0)) :
        parent[find(temp[i]-1)] = first
    party.append(temp)

truthSet = set()

for i in range(truth.pop(0)) :
    truthSet.add(find(truth[i]-1))

count = 0
for i in range(m) :
    if find(party[i][0]-1) in truthSet :
        pass
    else :
        count += 1

print(count)