#http://matplotlib.org/users/pyplot_tutorial.html
import matplotlib.pyplot as plt
import math

def plottest():
    plt.plot([1,2,3,4], [1,4,9,16], 'ro')
    plt.axis([0, 6, 0, 20])
    plt.show()


def plotlog():
    x=[]
    y1=[]
    y2=[]
    for i in range(1,20,1):
        x.append(i)
        y1.append(math.log(i))
        y2.append(i*math.log(i))
    plt.plot(x,y1,'r',x,y2)
    plt.annotate('nlog(n)', xy=(10, 2.23), xytext=(11, 7),
                 arrowprops=dict(facecolor='black', shrink=0.06),
                 )

    plt.annotate('log(n)', xy=(10, 23), xytext=(11, 24),
                 arrowprops=dict(facecolor='black', shrink=0.06),
                 )
    plt.show()

plotlog()

