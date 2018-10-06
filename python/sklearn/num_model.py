import numpy as nnp
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
iris_X = iris.date
iris_Y = iris.target

train_test_split(iris_X, iris_Y, test_size=0.3)
