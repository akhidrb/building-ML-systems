import matplotlib.pyplot as plt
import scipy as sp

class MyPlot:

    def error(slef, f, x, y):
        return sp.sum((f(x)-y)**2)

    def plotData(self, x, y):
        plt.scatter(x, y, s=10) #s=10 (dots in graph are of size=10)
        plt.title("Web traffic over the last month")
        plt.xlabel("Time")
        plt.ylabel("Hits/hour")
        plt.xticks( [w*7*24 for w in range(10)] , ['week %i' % w for w in range(10)])
        plt.autoscale(tight=True)
        plt.grid(True, linestyle='-', color='0.75')

    def plotStraightLine(self, x, y):
        fp1 = sp.polyfit(x, y, 1)
        self.f1 = sp.poly1d(fp1)
        fx = sp.linspace(0, x[-1], 1000)  #generates X-values for plotting
        plt.plot(fx, self.f1(fx), 'r-',linewidth=4)
        print("Straight Line:") 
        print("Model parameters: %s" % fp1)
        print("Error: %s" % self.error(self.f1, x, y))
    
    def plotTwoDegree(self, x, y):
        fp2 = sp.polyfit(x, y, 2)
        self.f2 = sp.poly1d(fp2)
        fx = sp.linspace(0, x[-1], 1000)  #generates X-values for plotting
        plt.plot(fx, self.f2(fx), 'g-',linewidth=4)
        print("Two Degrees:") 
        print("Model parameters: %s" % fp2)
        print("Error: %s" % self.error(self.f2, x, y))

    def showPlot(self):
        plt.legend(["d=%i" % self.f2.order], loc="upper left")
        plt.show()