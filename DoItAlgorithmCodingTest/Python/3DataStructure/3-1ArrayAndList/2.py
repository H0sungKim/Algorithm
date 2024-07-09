# 2021 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1546
# Difficulty :    브론즈I
# Problem :       평균

subNum = int(input())
scoreSet = input()

sum = 0
temp = list(map(int, scoreSet.split()))
for i in temp :
    sum += i  

print(sum/subNum/max(temp)*100)