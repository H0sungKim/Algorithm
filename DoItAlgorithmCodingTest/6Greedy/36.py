# 2022 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1541
# Difficulty :    실버II
# Problem :       잃어버린 괄호

expression = input()

result = 0
checkFirst = False
for i in expression.split("-") :

    if checkFirst :
        for j in i.split("+") :
            result = result - int(j)
    else :
        for j in i.split("+") :
            result = result + int(j)

    if not checkFirst :
        checkFirst = True

print(result)