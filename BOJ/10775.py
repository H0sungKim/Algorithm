# 2024 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/10775
# Difficulty :    골드II
# Problem :       공항

# Union Find

import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

airport = [i for i in range(g+1)]

def find(index) :
    if index < 0 :
        return index
    if airport[index] == index :
        return index
    airport[index] = find(airport[index])
    return airport[index]

for i in range(p) :
    airplane = int(input())
    airport[find(airplane)] -= 1
    if find(airplane) < 0 :
        print(i)
        exit()
    
print(p)