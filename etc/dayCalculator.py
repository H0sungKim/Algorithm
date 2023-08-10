# 2022 Hosung.Kim <hyongak516@mail.hongik.ac.kr>

day = 0

year = int(input("년을 입력하세요 : "))
month = int(input("월을 입력하세요 : "))
date = int(input("일을 입력하세요 : "))

for i in range((year-1)//400) :
    day += 146097
for i in range((year-1)%400//100) :
    day += 36524
for i in range((year-1)%400%100//4) :
    day += 1461
for i in range((year-1)%400%100%4) :
    day += 365

    
#각 월별 일수   1월|2월|3월|4월|5월|6월|7월|8월|9월|10월|11월|12월
monthDay =     [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#윤년 계산
#년도가 400으로 나누어 떨어지면 윤년
#년도가 400으로 나누어 떨어지지 않고 100으로 나누어 떨어지면 윤년
#년도가 100으로 나누어 떨어지지 않고 4로 나누어 떨어지면 윤년
if year%400 == 0 :
    monthDay[1] = 29
elif year%100 == 0 :
    monthDay[1] = 28
elif year%4 == 0 :
    monthDay[1] = 29
else :
    monthDay[1] = 28

for i in range(month-1) :
    day += monthDay[i]
day += date

print(day)
if day%7 == 0 :
    print("Sunday")
elif day%7 == 1 :
    print("Monday")
elif day%7 == 2 :
    print("Tuesday")
elif day%7 == 3 :
    print("Wednesday")
elif day%7 == 4 :
    print("Thursday")
elif day%7 == 5 :
    print("Friday")
elif day%7 == 6 :
    print("Saturday")