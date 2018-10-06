'''
    python 模块安装
    numpy：为python计算提供大量函数库
'''

'''
    python文件读写
'''
#写文件
text="This is my first text.\nThis a my text"
myFile = open('my file.txt','w')
myFile.write(text)
myFile.close()

#添加文件内容
appendText="\nThe new text"
myFile=open('my file.txt','a')
myFile.write(appendText)
myFile.close()

#读文件
'''
    open函数定义了一个指针，read()方法后指向末尾，之后的readline()和readlines()读不出内容
'''
file=open('my file.txt','r')
content=file.read()
print(content)

content=file.readline()
print(content)

content=file.readlines()
print(content)

'''
    python class
    调用：calculator=Calculator()
'''
class Calculator:
    o=1
    t=2
    def __init__(self,one,two):
        self.o=one      #__init__函数自己定义并初始化变量
        self.t=two
        self.add(Calculator.o,Calculator.t)
        
    def add(self,x,y):
        result=x+y
        print(result)
        return result

    def minus(self,x,y):
        result=x-y
        return result

    def times(self,x,y):
        result=x*y
        return result

    def divide(self,x,y):
        result=x/y
        return result


'''
    python input(返回字符串)
'''
a_input=input('Plaease give me a nunber')
print('The input number is',a_input)

'''
    python 元组 列表
    
'''
#元组
a_tuple=(1,2,3,4)
another_tuple=1,2,3,4

#列表
a_list=[1,2,3,4]
a_list.append(0)
print(a_list)
#(位置，值)；元组第一位是0；列表第一位是1
a_list.insert(1,0)
print(a_list)
#(第一个等于x的值)
a_list.remove(0)
print(a_list)
#输出最后一位的值
print(a_list[-1])
#输出0到3位
print(a_list[0:3])
#输出某一值的索引
print(a_list.index(1))
#输出某个值出现的次数
print(a_list.count(1))
#排序:从小到大排序
a_list.sort()
print(a_list)
#排序：从大到小排序
a_list.sort(reverse=True)
print(a_list)

'''
    pyhon 多维列表
    多维列表的计算可用numpy pandas 模块进行计算
'''
mun_dim_a=[[1,2,3],
           [3,4,1],
           [3,3,5]]
print(mun_dim_a[1])
print(mun_dim_a[1][2])

'''
    python 字典
'''
d={'apple':1,
   'pear':2,
   'orange':3,
   'fruit':
       {
       'one':'apple',
       'two':'orange'
       }
   }
d2={1:'a','b':'c'}

print(d['apple'])
print(d['fruit']['one'])
#删除字典
del d['orange']
print(d)
#添加字典;所添加内容没有顺序
d['b']=20
print(d)

