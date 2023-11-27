# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/1694
# Difficulty :    골드V
# Problem :       Chessboard in FEN

def isValidCoordinate(x, y) :
    if x < 0 or x > 7 or y < 0 or y > 7 :
        return False
    return True


def isBlank(piece) :
    if ord(piece) == 48 :
        return True
    else :
        return False

while True:
    try:
        temp = list(input().split("/"))
    except EOFError:
        break

    chessBoard = []
    for i in temp :
        line = ""
        for j in i :
            if j.isdigit() :
                line += "0" * int(j)
            else :
                line += j
        chessBoard.append(line)
    
    occupiedSquare = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    for x in range(8) :
        for y in range(8) :
                occupiedSquare[x][y] += 1
                if chessBoard[x][y] == "K" or chessBoard[x][y] == "k" :
                    for i in range(2) :
                        for j in range(2) :
                            for k in range(2) :
                                for l in range(2) :
                                    tempMove = (i * (-2*j+1) + x, k * (-2*l+1) + y)
                                    if isValidCoordinate(tempMove[0], tempMove[1]) :
                                        if isBlank(chessBoard[tempMove[0]][tempMove[1]]) :
                                            occupiedSquare[tempMove[0]][tempMove[1]] += 1

                elif chessBoard[x][y] == "Q" or chessBoard[x][y] == "q" :
                    for i in range(2) :
                        for j in range(2) :
                            for k in range(2) :
                                for l in range(2) :
                                    step = 1
                                    tempMove = (i * (-2*j+1) * step + x, k * (-2*l+1) * step + y)
                                    while isValidCoordinate(tempMove[0], tempMove[1]) :
                                        if isBlank(chessBoard[tempMove[0]][tempMove[1]]) :
                                            occupiedSquare[tempMove[0]][tempMove[1]] += 1
                                        else :
                                            break
                                        step += 1
                                        tempMove = (i * (-2*j+1) * step + x, k * (-2*l+1) * step + y)

                elif chessBoard[x][y] == "R" or chessBoard[x][y] == "r" :
                    for i in range(2) :
                        for j in range(2) :
                            step = 1
                            tempMove = ((1-i) * (-2*j+1) * step + x, i * (-2*j+1) * step + y)
                            while isValidCoordinate(tempMove[0], tempMove[1]) :
                                if isBlank(chessBoard[tempMove[0]][tempMove[1]]) :
                                    occupiedSquare[tempMove[0]][tempMove[1]] += 1
                                else :
                                    break
                                step += 1
                                tempMove = (1-i) * (-2*j+1) * step + x, i * (-2*j+1) * step + y

                elif chessBoard[x][y] == "N" or chessBoard[x][y] == "n" :
                    for i in range(2) :
                        for j in range(2) :
                            for k in range(2) :
                                tempMove = ((-2*j+1) * (1+i) + x, (-2*k+1) * (2-i) + y)
                                if isValidCoordinate(tempMove[0], tempMove[1]) :
                                    occupiedSquare[tempMove[0]][tempMove[1]] += 1

                elif chessBoard[x][y] == "B" or chessBoard[x][y] == "b" :
                    for i in range(2) :
                        for j in range(2) :
                            step = 1
                            tempMove = ((-2*i+1) * step + x, (-2*j+1) * step + y)
                            while isValidCoordinate(tempMove[0], tempMove[1]) :
                                if isBlank(chessBoard[tempMove[0]][tempMove[1]]) :
                                    occupiedSquare[tempMove[0]][tempMove[1]] += 1
                                else :
                                    break
                                step += 1
                                tempMove = ((-2*i+1) * step + x, (-2*j+1) * step + y)

                elif chessBoard[x][y] == "P" or chessBoard[x][y] == "p" :
                    color = (ord(chessBoard[x][y])-80)//32
                    for i in range(2) :
                        tempMove = (x + 2*color-1, 2*i-1+y)
                        if isValidCoordinate(tempMove[0], tempMove[1]) :
                            if isBlank(chessBoard[tempMove[0]][tempMove[1]]) :
                                occupiedSquare[tempMove[0]][tempMove[1]] += 1

                else :
                    occupiedSquare[x][y] -= 1
    
    occupiedSquareNum = 0
    for i in range(8) :
        for j in range(8) :
            if occupiedSquare[i][j] == 0 :
                occupiedSquareNum += 1

    print(occupiedSquareNum)