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
        features, feature_names, target, target_names = self.dataManager.structureData(data)
        self.plot.plotIrisData(features, target)
        self.plot.showPlot()


if __name__ == "__main__":
        main = Main()
        main.run()
    
