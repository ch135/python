import pandas as pd
import numpy as np

s=pd.Series([1,3,6,np.nan,44,1])

dates= pd.date_range('20160101',periods=6)

df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])

df1= pd.DataFrame(np.arange(12).reshape(3,4))

df2=pd.DataFrame({'A':1.,
                  'B':pd.Timestamp('20130102'),
                  'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                  'D':pd.Categorical(['test','train','test','train']),
                  'E':np.array([3]*4,dtype='int32'),
                  'F':'foo'
    })

print(s)

print(dates)

print(df)

print(df1)

print(df2)

print(df2.dtypes)

print(df2.index)

print(df2.columns)

print(df2.values)

print(df2.describe())

print(df2.T)

print(df2.sort_index(axis=1,ascending=False))   #对列排序 ascending=False:以倒的数列进行排序

print(df2.sort_values(by='E'))


'''
    pandas选取数据
'''

dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

print('1.\n')
print(df)

print('2.\n')
print(df['A'],df.A)     #取某一列值

print('3.\n')
print(df[0:3],df['20130101':'20130104'])        #取某几行的值

#select by label:loc
print('4.\n')
print(df.loc['20130102'])   #取某一列的值

print('5.\n')
print(df.loc['20130102',['A','B']])     #取某一行+列范围的值

#select by position iloc
print('6.\n')
print(df.iloc[3,1])   #取矩阵中的某一个值

print('7.\n')
print(df.iloc[[1,2,5],1:3])     #取某几行，再取对应某个范围的列（1<=列数<3）

print(df.iloc[3:5,1:3])

print('8\n')
print(df[df.A<8])

'''
    pandas 设置值
'''
df.iloc[2,2]=111

df.loc['20130101','B']=98

#df[df.A>4]=0
df.A[df.A>4]=0

df['F']=np.nan

df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))

print('9.\n')
print(df)

'''
    pandas 处理丢失数据
'''
print('10\n')
print(df.dropna(axis=0,how='any'))  #how=['any','all']  0:行；1：列

print(df.fillna(value=0))   #给null填充某个值

print(df.isnull())  #判断是否为null

print(np.any(df.isnull())==True)    #判断矩阵中是否有null
