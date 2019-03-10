
import scipy as sp
from scipy.optimize import fsolve
from sklearn.datasets import load_iris

class DataManager:

    def getData(self):
        return load_iris()

    def structureData(self, data):
        features = data.data
        feature_names = data.feature_names
        target = data.target
        target_names = data.target_names
        return features, feature_names, target, target_names

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
        