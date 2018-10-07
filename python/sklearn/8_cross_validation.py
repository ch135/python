from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
Y = iris.target

# 测试训练误差
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)
print(knn.score(X_test, Y_test))

# 交叉验证评分
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, Y, cv=5, scoring='accuracy')
print(scores)

# 使用交叉验证判断选择哪些模型或属性
k_range = range(1, 31)
k_scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    loss = -cross_val_score(knn, X, Y, cv=10, scoring='neg_mean_squared_error')
    # scores = cross_val_score(knn, X, Y, cv=10, scoring='accuracy')
    k_scores.append(loss.mean())

plt.plot(k_range, k_scores)
plt.xlabel('The value of K for KNN')
plt.ylabel('Cross-Validated Loss')
plt.show()