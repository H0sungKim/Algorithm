# 2021 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1546
# Difficulty :    브론즈I
# Problem :       평균

n = int(input())
scoreList = list(map(int, input().split()))

sum = 0
for i in scoreList :
    sum += i  

print(sum/n/max(scoreList)*100)