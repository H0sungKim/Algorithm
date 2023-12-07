# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1300
# Difficulty :    골드I
# Problem :       K번째 수

# BinarySearch

n = int(input())
k = int(input())

start = 1
end = k

while start <= end :
    mid = (start+end)//2
    count = 0
    for i in range(n) :
        count += min(mid//(i+1), n)

    if count < k :
        start = mid + 1
    else :
        end = mid - 1

print(start)