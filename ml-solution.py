from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD
from pyspark.mllib.classification import LogisticRegressionWithSGD

from pyspark import SparkContext
from pyspark.mllib.linalg import Vectors

def check ( d ):
   if d == "?":
     return 0.0
   else:
     return float(d)

def process( row ):
   trimmed = row#.replace("\"","")
   label   = int(trimmed[-1])
   features = map(check, trimmed[4:])
   return LabeledPoint(label, Vectors.dense(features))


sc = SparkContext("local[2]", "First Spark App")
rdd = sc.textFile("train.tsv")
rdd = rdd.map( lambda x: x.replace("\"",""))
rdd = rdd.map( lambda x: x.split("\t"))
res = rdd.map(process)

numIterations = 10
maxTreeDepth = 5

lrModel = LogisticRegressionWithSGD.train( res, numIterations)

datapoint = res.first()
print lrModel.predict(datapoint.features)
