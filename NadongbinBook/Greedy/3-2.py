# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
# 
# ==============
# Greedy
# 3-2
# --------------
# 문제 92p
# 정답 95p
# ==============

n, m, k = map(int, input().split())

num = list(map(int, input().split()))

num.sort()

first = num[-1]
second = num[-2]

result = 0

result += m//(k+1) * second
result += (m - m//(k+1)) * first

print(result)