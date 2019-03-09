
import scipy as sp

class DataManager:

    def getData(self):
        return sp.genfromtxt("web-traffic.tsv", delimiter="\t")

    def structureData(self, data):
        x = data[:,0]
        y = data[:,1]
        x = x[~sp.isnan(y)]
        y = y[~sp.isnan(y)]
        return x, y