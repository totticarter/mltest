#coding:utf-8
import numpy as np
import os
import matplotlib.pyplot as plt
def drawScatterDiagram(fileName):
    #改变工作路径到数据文件存放的地方
    os.chdir("E:\\bigdata\\ml\\als\\data")
    xcord = []
    ycord = []
    fr=open(fileName)
    for line in fr.readlines():
        lineArr=line.strip().split()
        if len(lineArr)==0:
            break
        xcord.append(float(lineArr[1]));ycord.append(float(lineArr[2]))
    plt.scatter(xcord,ycord,s=30,c='red',marker='s')
    plt.show()

drawScatterDiagram("data.txt")