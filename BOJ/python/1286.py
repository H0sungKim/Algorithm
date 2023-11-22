# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1286
# Difficulty :    골드V
# Problem :       부분 직사각형

n, m = map(int, input().split())

rectangle = []

for i in range(n) :
    rectangle.append(input())

count = [0] * (ord('Z') - ord('A') + 1)

for i in range(n) : 
    for j in range(m) :
        letterCount = (j+1) * (i+1) * (2*n-i) * (2*m-j)
        count[ord(rectangle[i][j])-ord('A')] += letterCount
        count[ord(rectangle[n-i-1][j])-ord('A')] += letterCount
        count[ord(rectangle[i][m-j-1])-ord('A')] += letterCount
        count[ord(rectangle[n-i-1][m-j-1])-ord('A')] += letterCount

for i in count :
    print(i)