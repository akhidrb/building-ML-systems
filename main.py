import numpy as np
import scipy as sp

import matplotlib.pyplot as plt

from myPlot import MyPlot
from dataOrganizer import DataManager

class Main:
    def __init__(self):
        self.dataOrganizer = DataManager()
        self.plot = MyPlot()

    def run(self):
        data = self.dataOrganizer.getData();    
        x, y = self.dataOrganizer.structureData(data)
        self.plot.plotData(x, y)
        self.plot.plotStraightLine(x, y)
        self.plot.plotTwoDegree(x, y)
        self.plot.showPlot()


if __name__ == "__main__":
        main = Main()
        main.run()
    
