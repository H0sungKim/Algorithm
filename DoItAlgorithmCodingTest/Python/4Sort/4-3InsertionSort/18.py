# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11399
# Difficulty :    실버IV
# Problem :       ATM

n = int(input())

time = list(map(int, input().split()))

for i in range(1, n) :
    insertPoint = i
    insertValue = time[i]
    for j in range(i) :
        if time[i] < time[j] :
            insertPoint = j
            break
    for j in range(i-insertPoint) :
        time[i-j] = time[i-j-1]
    time[insertPoint] = insertValue

result = 0
for i in range(n) :
    result += (n-i) * time[i]

print(result)