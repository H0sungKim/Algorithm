# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/2718
# Difficulty :    골드I
# Problem :       타일 채우기

caseNum = int(input())

tileCase = [[1, 0, 0, 0], [1, 2, 1, 1], [5, 4, 1, 1]]
CASE1 = 0 # @@ @@
CASE2 = 1 # @@ @ @ | @ @ @@
CASE3 = 2 # @ @@ @
CASE4 = 3 # @ @ @ @

for i in range(caseNum) :
    n = int(input())
    if n <= len(tileCase) :
        print(sum(tileCase[n-1]))
        continue

    length = len(tileCase)
    while length < n :
        tileCase.append([sum(tileCase[length-1]), 2*tileCase[length-1][CASE1]+tileCase[length-1][CASE2], tileCase[length-1][CASE1]+tileCase[length-2][CASE3], tileCase[length-1][CASE1]])
        length = len(tileCase)
    print(sum(tileCase[n-1]))