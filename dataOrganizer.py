
import scipy as sp
from scipy.optimize import fsolve

class DataManager:

    def getData(self):
        return sp.genfromtxt("web-traffic.tsv", delimiter="\t")

    def structureData(self, data):
        x = data[:,0]
        y = data[:,1]
        x = x[~sp.isnan(y)]
        y = y[~sp.isnan(y)]
        return x, y

    def dataAfterInflection(self, x, y):
        inflection = int(3.5*7*24)   # 3.5 is the number of weeks before inflection
        xa = x[inflection:]
        ya = y[inflection:]
        return xa, ya

    def predict(self, x, y):
        fp2 = sp.polyfit(x, y, 2)
        fbt2 = sp.poly1d(fp2)
        reached_max = fsolve(fbt2 - 100000, x0=800) / (7*24)
        print("100,000 hits/hour expected at week %f" % reached_max[0])
        