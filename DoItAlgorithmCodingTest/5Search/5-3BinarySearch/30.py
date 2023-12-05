# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2343
# Difficulty :    실버I
# Problem :       기타 레슨

n, m =  map(int, input().split())

lecture = list(map(int, input().split()))

lectureSum = sum(lecture)

start = max(lectureSum // m, max(lecture))
end = lectureSum

while start <= end :
    mid = (start+end) // 2
    temp = 0
    count = 1
    for i in lecture :
        if temp + i > mid :
            count += 1
            temp = i
        else :
            temp += i
    if count > m :
        start = mid+1
    else :
        end = mid-1

print(start)