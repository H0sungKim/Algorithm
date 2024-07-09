# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11505
# Difficulty :    골드I
# Problem :       구간 곱 구하기

import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m, k = map(int, input().split())
treeHeight = 0
MAXVALUE = 1000000007

temp = n-1
while temp :
    temp //= 2
    treeHeight += 1

treeSize = 2**(treeHeight+1)
tree = [1 for _ in range(treeSize)]
leafStart = treeSize//2

for i in range(n) :
    tree[leafStart+i] = int(input())

temp = leafStart//2
for i in range(treeHeight) :
    for j in range(temp) :
         tree[temp+j] = tree[(temp+j)*2] * tree[(temp+j)*2+1] % MAXVALUE
    temp //= 2

def changeValue(index, value) :
    index = leafStart+index-1
    tree[index] = value
    while index > 0 :
        index //= 2
        tree[index] = tree[index*2] * tree[index*2+1] % MAXVALUE
    
def getMultiply(start, end) :
    start = leafStart+start-1
    end = leafStart+end-1
    result = 1
    while start <= end :
        if start%2 == 1 : 
            result *= tree[start]
            start += 1
        if end%2 == 0 :
            result *= tree[end]
            end -= 1
        start //= 2
        end //= 2
        result %= MAXVALUE
    return result

for _ in range(m+k) :
    a, b, c = map(int, input().split())
    if a == 1 :
        changeValue(b, c)
    if a == 2 :
        print(f"{getMultiply(b, c)}\n")