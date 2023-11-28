# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/12865
# Difficulty :    골드V
# Problem :       평범한 배낭
# 
# 
# Knapsack Algorithm
# 
# ns[N][K] is the maximum value when the items up to the Nth are determined to be included or not and the K weight is filled in the bag.

n, k = map(int, input().split())

item = []

for i in range(n) :
    item.append(list(map(int, input().split())))

# TimeOut ======================================
# Explore all cases
# maxValue = 0
# for i in range(2**n) :
#     tempValue = 0
#     tempWeight = 0
#     for j in range(n) :
#         if 1 << j & i != 0 :
#             tempWeight += item[j][0]
#             tempValue += item[j][1]
#     if tempWeight <= k :
#         if tempValue > maxValue :
#             maxValue = tempValue
#
# print(maxValue)


ns = [[0 for i in range(k+1)] for j in range(n+1)]

for i in range(1, n+1) :
    for j in range(1, k+1) :
        tempWeight = item[i-1][0]
        tempValue = item[i-1][1]
        if j >= tempWeight :
            ns[i][j] = max(ns[i-1][j], ns[i-1][j-tempWeight]+tempValue)
        else :
            ns[i][j] = ns[i-1][j]

print(ns[n][k])