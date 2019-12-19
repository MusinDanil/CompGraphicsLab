import pylab

Xlist = []
Ylist = []

with open('input.txt', mode='r') as input:
    for line in input:
        temp = line.split(';')
        Xlist.append(float(temp[0]))
        Ylist.append(float(temp[1]))

pylab.plot(Xlist, Ylist)

pylab.show()
