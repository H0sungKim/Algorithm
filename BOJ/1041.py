# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1041
# Difficulty :    골드V
# Problem :       주사위

n = int(input())

dice = list(map(int, input().split()))

dice2FaceMin = 100
for i in range(5) :
    for j in range(i+1, 6) :
        if i+j == 5 :
            continue
        if dice[i]+dice[j] < dice2FaceMin :
            dice2FaceMin = dice[i]+dice[j]

dice3FaceMin = 150
for i in range(4) :
    for j in range(i+1,5) :
        for k in range(j+1,6) :
            if i+j == 5 or j+k == 5 or k+i == 5 :
                continue
            if dice[i]+dice[j]+dice[k] < dice3FaceMin :
                dice3FaceMin = dice[i]+dice[j]+dice[k]

result = 0

# Vertex
if n == 1 :
    print(sum(dice)-max(dice))
    exit()
else :
    result += dice3FaceMin*4 + dice2FaceMin*4

# Edge
if n-2>0 :
    result += 8 * (n-2) * dice2FaceMin + 4 * (n-2) * min(dice)

# Face
if n-2>0 :
    result += 5 * (n-2) * (n-2) * min(dice)

print(result)