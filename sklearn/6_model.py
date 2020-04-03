from sklearn import datasets
from sklearn.linear_model import LinearRegression

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_Y = loaded_data.target

model = LinearRegression()
model.fit(data_X, data_Y)

# e.g y=2x + 3，输出2
print(model.coef_)
# e.g y=2x + 3，输出3
print(model.intercept_)
# 输出LinearRegression()的配置属性
print(model.get_params())
# 对预测值与输出值进行打分
#   LinearRegression的打分标准为：
#      R^2 coefficient of determination
print(model.score(data_X, data_Y))