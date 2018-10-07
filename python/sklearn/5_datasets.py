from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 加载数据
load_data = datasets.load_boston()
data_X = load_data.data
data_Y = load_data.target

# 创建模型
model = LinearRegression()
model.fit(data_X, data_Y)

# print(model.predict(data_X[:4, :]))
# print(data_Y[:4])

# 创建虚拟数据
X, Y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=1)

plt.scatter(X, Y)
plt.show()