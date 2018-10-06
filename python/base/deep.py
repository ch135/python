"""
    python 模块加载
"""
#way one
import time

print(time.localtime())

#way two
import time as t
print(t.localtime())

#way three
from time import time,localtime
print(localtime())

#way four
from time import *
print(time())

"""
    python 创建自己的模块
    模块可放置到自己定义的目录，也可放到python默认目录下（site-packages）
    
"""
import model

model.text()

"""
    python 错误处理:
    try 
"""
try:
    file=open('111','r+')
except Exception as e:
    print('文件不存在')
    response=input('do you wanr creat a book?')
    if response=='y':
        file=open('111','w')
    else:
        pass
else:
    file.write('错误测试')
file.close()

"""
    python
    zip：数组集合器
    lambpa：可快速创建函数
    map：将函数与参数绑定在一起
"""
#zip
a=[1,2,3]
b=[4,5,6]

print(list(zip(a,b)))
print(list(zip(a,b,b)))

for i, j in list(zip(a,b)):
    print(i*2,j/2)

#lambda
fun2=lambda x,y:x+y
5
print(fun2(2,3))
#map
print(list(map(fun2,[2,3],[4,5])))

"""
    python在多层数列中
    copy:第一层数列索引不一样，第二层索引一样
    deepcopy：数列的每层索引都不一样
"""
import copy
a=[1,2,3,[1,2]]
b=copy.copy(a)
print(id(a)==id(b))
print(id(a[3])==id(b[3]))

c=copy.deepcopy(a)
print(id(a[3])==id(c[3]))

"""
    python multiprocessing多核运算
"""

"""
    python tkinter开发可视化窗口
"""

"""
    python pickle存放处理结果到文件中
"""
import pickle
data={
    'a':[1,2,3,4,5,6],
    'b':[1,2,3,4],
    'c':[1,2,3]
    }

with open('data.pickle','wb') as f:
    pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)

with open('data.pickle','rb') as f:
    data=pickle.load(f)
    print(data)

"""
    python set
"""
char_list=['a','b','a']
print(set(char_list))

"""
    python Reggex正则表达式（可用于爬虫）
"""
import re
# re.search(str1,str2)
