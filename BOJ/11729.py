# 2023 Hosung.Kim <hyongak516@mail.hongik.ac.kr>
#
# URL :           https://www.acmicpc.net/problem/11729
# Difficulty :    골드V
# Problem :       하노이 탑 이동 순서


# n+1
#
# n (2 <-> 3)
# 1 3
# n (1 <-> 2)


def hanoiTower(depth, oldHanoi) :
    if depth == 1 :
        result = ""
        result += str(len(oldHanoi)//2) + "\n"
        for i in range(len(oldHanoi)) :
            result += oldHanoi[i]
            if i%2 == 0 :
                result += " "
            else :
                if i == len(oldHanoi)-1 :
                    continue
                result += "\n"
        return result
    
    newHanoi1 = ""
    newHanoi2 = ""
    for i in range(len(oldHanoi)) :
        if oldHanoi[i] == "1" :
            newHanoi1 = newHanoi1 + "1"
            newHanoi2 = newHanoi2 + "2"
        elif oldHanoi[i] == "2" :
            newHanoi1 = newHanoi1 + "3"
            newHanoi2 = newHanoi2 + "1"
        elif oldHanoi[i] == "3" :
            newHanoi1 = newHanoi1 + "2"
            newHanoi2 = newHanoi2 + "3"
            
    return hanoiTower(depth-1, newHanoi1+"13"+newHanoi2)

disk = int(input())
firstHanoi = "13"
print(hanoiTower(disk, firstHanoi))