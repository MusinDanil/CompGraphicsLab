from math import sin
from numpy import arange

dots = []
for x in arange(-5, 3, 0.01):
    y = 2 ** x * sin(2 ** (-x))
    dots.append((x, y))

with open('input.txt', mode='w') as file:
    for dot in dots:
        file.write(str(dot[0]) + ';' + str(dot[1]) + '\n')
