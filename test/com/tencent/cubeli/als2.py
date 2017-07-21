# -*- coding: utf-8 -*
import numpy as np
import os
import matplotlib.pyplot as plt

def getab(fileName):
    os.chdir("E:\\bigdata\\ml\\als\\data")
    xcord = [];ycord = []
    fr = open(fileName)
    xy_a=0.0;x2_a=0.0;x_a=0.0
    y_b=0.0;x_b=0.0;bcount=0
    for line in fr.readlines():
        lineArr=line.strip().split()
        # print len(lineArr)
        if len(lineArr)==0:
            break
        xy_a += float(lineArr[1]) * float(lineArr[2]);x2_a += float(lineArr[1]) * float(lineArr[1]);x_a += float(lineArr[1])
        y_b += float(lineArr[2]);x_b += float(lineArr[1]);bcount += 1

    c11=x2_a*x_b;c12=x_a*x_b
    c21=x_b*x2_a;c22=0-bcount*x2_a
    d=xy_a-y_b
    b=(d/(c12+c22))
    a=(b+y_b)/x_b
    print a
    print b


def drawScatterDiagram(fileName):
    #改变工作路径到数据文件存放的地方
    os.chdir("E:\\bigdata\\ml\\als\\data")
    xcord=[];ycord=[]
    fr=open(fileName)
    for line in fr.readlines():
        lineArr=line.strip().split()
        if len(lineArr)==0:
            break
        xcord.append(float(lineArr[1]));ycord.append(float(lineArr[2]))
    plt.scatter(xcord,ycord,s=30,c='red',marker='s')
    #a=0.1965;b=-14.486
    a=0.1612;b=-8.6394
    x=np.arange(90.0,250.0,0.1)
    y=a*x+b
    plt.plot(x,y)
    plt.show()

getab("data.txt")
# drawScatterDiagram("data.txt")