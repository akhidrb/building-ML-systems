
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

        