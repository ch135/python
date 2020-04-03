import numpy as np

array= np.array([[1,2,3],
                [4,5,6]])

print(array)
print('number of dim',array.ndim)
print('shape',array.shape)
print('size',array.size)


'''
    numpy 创建数组 矩阵
'''
a=np.array([2,2,4],dtype=np.int)

print(a.dtype)

b=np.array([[1,2,3],[4,56,10]])
print(b)

c=np.zeros((3,4))
print(c)

d=np.ones((3,4),dtype=np.int)
print(d)

e=np.empty((3,4))
print(e)

f=np.arange(10,22).reshape((3,4))
print(f)

g=np.linspace(1,10,6).reshape((2,3))   #生成线段
print(g)

'''
    numpy 基本计算
'''
a=np.array([1,2,3,4,])

b=np.arange(4)

print(a)
print(b)

c=a+b
print(c)
print(c*c)

d=10*np.sin(a)
print(d)

print(d<1)


e=np.array([[1,2,3],[4,5,6]])
f=np.arange(6).reshape(3,2)

print(e.dot(f)) #矩阵乘法

g=np.random.random((2,4))

print("g=",g)
print(np.sum(g))
print(np.min(g))
print(np.max(g))
print(np.sum(g,axis=1))     #1：矩阵的行；0：矩阵的列
print(np.min(g,axis=0))
print(np.max(g,axis=1))

A=np.arange(2,14).reshape(3,4)

print(A)

print(np.argmin(A)) #输出最小索引

print(np.argmax(A)) #输出最大索引

print(np.average(A))    #输出平均值

print(np.median(A))     #输出中位数

print(np.cumsum(A))     #输出累加

print(np.diff(A))   #输出累差

print(np.nonzero(A))    #输出非零数


print(np.sort(A))   #矩阵排序

print(np.transpose(A))  #矩阵转置

print(A.T)

print(np.clip(A,5,9))   #矩阵值保留在5~9，不在的自己变化

print(np.mean(A,axis=1))    #对行求平均值


'''
    numpy 索引
'''
B=np.arange(3,15).reshape(3,4)

print(A)

print(A[2][1])

print(A[1,:])

print(A[:,1])

print(A[:,1:2]) #所有行，1<=索引<2的值

for column in A.T:
    print(column)

print(A.flatten())  #将多行矩阵转化为单行多列矩阵

for item in A.flat: #迭代A的每一个选项
    print(item)

'''
    numpy array 合并
'''
A=np.array([1,1,1])
B=np.array([2,2,2])

C=np.vstack((A,B))  #上下合并
D=np.hstack((A,B))    #左右合并

print(A.shape,C)

print(D,D.shape)

print(A[:,np.newaxis])  #给A添加维度,左右合并不会成一行

A=np.array([1,1,1])[:,np.newaxis]
B=np.array([2,2,2])[:,np.newaxis]

C=np.hstack((A,B))
print(C)

C=np.concatenate((A,B,B,A),axis=1) #多行合并，并可以设置列或行合并
print(C)

'''
    numpy array 分割
'''
A=np.arange(2,14).reshape((3,4))

print(A)

print(np.split(A,3,axis=0)) #列不要动，对行分割

print(np.array_split(A,3,axis=1))

print(np.vsplit(A,3))   #横向分割

print(np.hsplit(A,2))   #纵向分割

'''
    numpy copy and deepcopy
'''

a=np.array([1,2,3,4])

b=a

print(a is b)
print(a)

b=a.copy() #deep copy
