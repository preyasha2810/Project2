# from statistics import mean
from StaticMethods.CaclulateMode import calMode
from StaticMethods.CalculateMedian import calMedian
from StaticMethods.CalulcateMean import calMean
from StaticMethods.PopulationCorrelationCoefficient import calcPCC
from StaticMethods.PopulationStandardDeviation import stddev
from StaticMethods.PopulationVariance import varpp
from StaticMethods.Zscore import zscore
from StaticMethods.confidenceInterval import confidenceInterval
from StaticMethods.varianceproportion import varProportion


class StatisticCal:
    result = 0

    def __init__(self):
        pass

    def mean(self, arr):
        self.result = calMean(arr)
        return self.result

    def median(self, arr):
        self.result = calMedian(arr)
        return self.result

    def mode(self, arr):
        self.result = calMode(arr)
        return self.result

    def sd(self, a):
        self.result = stddev(a)
        return self.result

    def vpp(self, a):
        self.result = varpp(a)
        return self.result

    def zscore(self, a, mean, sd):
        self.result = zscore(a, mean, sd)
        return self.result

    def pcc(self, a, b):
        self.result = calcPCC(a, b)
        return self.result

    def confInt(self, a, val):
        self.result = confidenceInterval(a, val)
        return self.result

    def varProp(self, a, c):
        self.result = varProportion(a, c)
        return self.result
