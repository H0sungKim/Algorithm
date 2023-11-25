# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1385
# Difficulty :    플래티넘V
# Problem :       벌집



# Floor : distance from 1
# UniqueNumber : refer to the picture below
#       __
#    __/ 1\__
#   / 6\__/ 2\
#   \__/  \__/
#   / 5\__/ 3\
#   \__/ 4\__/
#      \__/
# 
# the number of each tile : 1 + UniqueNumber*Floor + 3*Floor*(Floor-1)

# x-axis, y-axis, z-axis
#       __
#    __/  \__
#   / x\__/ y\
#   \__/  \__/
#   /  \__/  \
#   \__/ z\__/
#      \__/
# 
# z-axis can also be expressed as -x-axis-y-axis.


def getCoordinate(num) :
    i = 0
    while 1 + 3*i*(i+1) < num :
        i += 1
    floor = i

    for i in range(1, 7) :
        if i*floor + 3*floor*(floor-1) + 1 >= num :
            distanceFromI = num - ((i-1)*floor + 3*floor*(floor-1) + 1)
            match i :
                case 1 :
                    x = floor
                    y = distanceFromI
                case 2 :
                    x = floor-distanceFromI
                    y = floor
                case 3 :
                    x = -distanceFromI
                    y = floor - distanceFromI
                case 4 :
                    x = -floor
                    y = -distanceFromI
                case 5 :
                    x = distanceFromI-floor
                    y = -floor
                case 6 :
                    x = distanceFromI
                    y = distanceFromI-floor
            break
    return [x, y]

def getNum(x, y) :
    if x == 0 and y == 0 :
        return 1
    if x*y < 0 :
        floor = abs(x) + abs(y)
    else :
        floor = max(abs(x), abs(y))
    tempNum = 3*floor*(floor+1) + 1
    tempX = floor
    tempY = 0
    if tempX == x and tempY == y :
            return tempNum
    for i in range(floor) :
        tempX -= 1
        tempY -= 1
        tempNum -= 1
        if tempX == x and tempY == y :
            return tempNum
    for i in range(floor) :
        tempX -= 1
        tempNum -= 1
        if tempX == x and tempY == y :
            return tempNum
    for i in range(floor) :
        tempY += 1
        tempNum -= 1
        if tempX == x and tempY == y :
            return tempNum
    for i in range(floor) :
        tempX += 1
        tempY += 1
        tempNum -= 1
        if tempX == x and tempY == y :
            return tempNum
    for i in range(floor) :
        tempX += 1
        tempNum -= 1
        if tempX == x and tempY == y :
            return tempNum
    for i in range(floor) :
        tempY -= 1
        tempNum -= 1
        if tempX == x and tempY == y :
            return tempNum
    
a, b = map(int, input().split())

aCoordinate = getCoordinate(a)
bCoordinate = getCoordinate(b)
move = []
for i in range(2) :
    move.append(bCoordinate[i] - aCoordinate[i])

if move[0] * move[1] > 0 :
    move.append(-1 * move[int(abs(move[0]) > abs(move[1]))])
    move[0] += move[2]
    move[1] += move[2]

print(a, end="")
for i in range(len(move)) :
    for j in range(abs(move[i])) :
        if i == 2 :
            aCoordinate[0] -= 2*int(move[i]>0)-1
            aCoordinate[1] -= 2*int(move[i]>0)-1
        else :
            aCoordinate[i] += 2*int(move[i]>0)-1
        print(end=" ")
        print(getNum(aCoordinate[0], aCoordinate[1]), end="")
print()