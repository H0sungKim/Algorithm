# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1947
# Difficulty :    골드III
# Problem :       선물 전달

#   N   ANSWER
# ------------
#   1        0     *2-1
#   2        1     *3-1
#   3        2     *4+1
#   4        9     *5-1
#   5       44

n = int(input())

result = 0

for i in range(2, n+1) :
    result *= i
    result += -2*(i%2)+1
    result %= 1000000000

print(result)