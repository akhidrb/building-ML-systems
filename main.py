import numpy as np
import scipy as sp

import matplotlib.pyplot as plt

from myPlot import MyPlot
from dataOrganizer import DataManager

class Main:
    def __init__(self):
        self.dataManager = DataManager()
        self.plot = MyPlot()

    def run(self):
        data = self.dataManager.getData();    
        x, y = self.dataManager.structureData(data)
        xa, ya = self.dataManager.dataAfterInflection(x, y)
        
        self.dataManager.predict(xa, ya)

        self.plot.plotData(x, y)
        self.plot.plotTwoDegree(xa, ya)
        self.plot.showPlot()


if __name__ == "__main__":
        main = Main()
        main.run()
    
