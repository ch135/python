from sklearn.svm import SVC
from sklearn.datasets import load_iris
import pickle
from sklearn.externals import joblib

iris = load_iris()
X, Y = iris.data, iris.target
# 定义一个分类器
clf = SVC(gamma='auto')
clf.fit(X, Y)

# method 1:pickle
# save
with open('save/clf.pickle', 'wb',) as f:
    pickle.dump(clf, f)
# restore
with open('save/clf.pickle', 'rb') as f:
    clf2 = pickle.load(f)
    print(clf2.predict(X[0:1]))

# method 2:joblib
# joblib支持多线程存储数据

# save
joblib.dump(clf, 'save/clf.pkl')

# restore
clf3 = joblib.load('save/clf.pkl')
print(clf3.predict(X[0:1]))