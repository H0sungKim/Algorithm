# 2021 Hosung.Kim <hyongak516@mail.hongik.ac.kr>

size = int(input())
        
starLst = []
for i in range(size) :
    starLst.append(i+1)
        
def drawStar(num) :
    if starLst[num-1] == num :
        if num == 0 :
            return "*"
        elif num == 1 :
            starLst[num-1] = ["***", "* *", "***"]
            return ["***", "* *", "***"]
        else :
            temp = []
            for i in range(3**num) :
                if i//3**(num-1) == 2 :
                    temp.append(3*drawStar(num-1)[i%3**(num-1)])
                elif i//3**(num-1) == 1 :
                    temp.append(drawStar(num-1)[i%3**(num-1)] + 3**(num-1)*" " + drawStar(num-1)[i%3**(num-1)])
                elif i//3**(num-1) == 0 :
                    temp.append(3*drawStar(num-1)[i%3**(num-1)])
            starLst[num-1] = temp
            return temp
    else :
        return starLst[num-1]
    
product = drawStar(size)
for i in product :
    print(i)