import matplotlib.pyplot as plt
import scipy as sp

class MyPlot:

    def error(slef, f, x, y):
        return sp.sum((f(x)-y)**2)

    def setPlot(self, xLabel, yLabel):
        plt.title("Iris Data")
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)

    def plotIrisData(self, features, target):
        for t in range(3):
            if t == 0:
                c = 'r'
                marker = '>'
            elif t == 1:
                c = 'g'
                marker = 'o'
            elif t == 2:
                c = 'b'
                marker = 'x'
            plt.scatter(features[target == t,0], features[target == t,1], marker=marker, c=c)

    def showPlot(self):
        plt.show()