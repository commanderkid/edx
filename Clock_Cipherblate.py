from math import *
otvet = []
sluchai = int(input())
stroka = [x.split(':') for x in input().split()]
for i in range(sluchai):
    for j in range(len(stroka[i])):
        stroka[i][j] = int(stroka[i][j])
    xm = round(10 + 9 * sin(radians(6 * stroka[i][1])), 8)
    ym = round(10 + 9 * cos(radians(6 * stroka[i][1])), 8)
    hour = (360 * (60 * stroka[i][0] + stroka[i][1]))/ 720
    xh = round(10 + 6 * sin(radians(hour)), 8)
    yh = round(10 + 6 * cos(radians(hour)), 8)
    otvet += [xh, yh, xm, ym]
print(*otvet)
