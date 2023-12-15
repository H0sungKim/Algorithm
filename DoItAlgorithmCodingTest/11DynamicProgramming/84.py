# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1463
# Difficulty :    실버III
# Problem :       1로 만들기

# 1 2 3 4 5 6 7
# 0 1 1 2 3 2 3

answer = [0]

num = int(input())

for i in range(2, num+1) :
    temp = []
    temp.append(answer[i-2])
    if i % 2 == 0 :
        temp.append(answer[i//2-1])
    if i % 3 == 0 :
        temp.append(answer[i//3-1])
    answer.append(min(temp)+1)

print(answer[num-1])