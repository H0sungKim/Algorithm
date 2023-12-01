# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
# 
# ==============
# Greedy
# 3-1
# --------------
# 문제 87p
# 정답 90p
# ==============

n = 1260
count = 0

coin = [500, 100, 50, 10]

for i in coin :
    count += n//i
    n  %= i

print(count)