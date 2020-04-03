import pandas as pd
import numpy as np

'''
    pandas 导入导出
'''
data=pd.read_csv('get.csv')

print(data)

data.to_pickle('get.pickle')


'''
    pandas 合并concat
'''

#concatenating
df1=pd.DataFrame(np.zeros((3,4)),columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4)),columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])

res1=pd.concat([df1,df2,df3],axis=0)
res2=pd.concat([df1,df2,df3],axis=0,ignore_index=True)

print('1.\n')
print(res1)
print(res2)

#join.['inner','outer']
df1=pd.DataFrame(np.zeros((3,4)),columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4)),columns=['b','c','d','e'],index=[2,3,4])

print('2.\n')
print(df1)
print(df2)

res1=pd.concat([df1,df2],join='outer',sort='False',ignore_index=True)   #数据库自然链接
res2=pd.concat([df1,df2],join='inner',sort='False',ignore_index=True)   #数据库自然链接

print(res1)
print(res2)

#join_axes
df1=pd.DataFrame(np.zeros((3,4)),columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4)),columns=['b','c','d','e'],index=[2,3,4])

res1=pd.concat([df1,df2],axis=1,join_axes=[df1.index])  #指定某一矩阵的索引进行填充对应的空值

print('3.\n')
print(res1)

#append
df1=pd.DataFrame(np.zeros((3,4)),columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4)),columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['b','c','d','e'],index=[2,3,4])

res1=df1.append(df2,ignore_index=True,sort=False)
res2=df1.append([df2,df3],sort=False)

s1=pd.Series([1,2,3,4],index=['a','b','c','d'])

res3=df1.append(s1,ignore_index=True,sort=False)

print('4.\n')
print(res1)
print(res2)
print(res3)

#merging two df by key/keys.(may bre use in database)
#simple example
left=pd.DataFrame({'key':['K0','K1','K2','K3'],
                   'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3']
    })
right=pd.DataFrame({'key':['K0','K1','K2','K3'],
                   'C':['C0','C1','C2','C3'],
                   'D':['D0','D1','D2','D3']
    })

res1=pd.merge(left,right)

print('5.\n')
print(res1)

#consider two keys
left=pd.DataFrame({'key1':['K0','K1','K2','K3'],
                   'key2':['K0','K1','K0','K1'],
                   'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3']
    })
right=pd.DataFrame({'key1':['K0','K1','K2','K3'],
                    'key2':['K0','K0','K0','K30'],
                   'C':['C0','C1','C2','C3'],
                   'D':['D0','D1','D2','D3']
    })

#how=['left','right','outer','inner']
res1=pd.merge(left,right,on=['key1','key2'],how='inner')
res2=pd.merge(left,right,on=['key1','key2'],how='left')
res3=pd.merge(left,right,on=['key1','key2'],how='right')
res4=pd.merge(left,right,on=['key1','key2'],how='outer')

print('6.\n')
print(res1)
print(res2)
print(res3)
print(res4)

#indicator
df1=pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df2=pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})

print('7.\n')
print(df1)
print(df2)

res1=pd.merge(df1,df2,on='col1',how='outer',indicator=True) #indeicator= True 表示出左、右或两边都有数据
print(res1)

#give the indicator a custom name
res=pd.merge(df1,df2,on='col1')

#merged by index
left=pd.DataFrame({'A':['A0','A1','A2'],
                   'B':['B0','B1','B2']},
                  index=['K0','K1','K2'])
right=pd.DataFrame({'C':['C0','C1','C2'],
                   'D':['D0','D1','D2']},
                   index=['K0','K2','K3'])

#left_index and right_index
res1= pd.merge(left,right,left_index=True,right_index=True,how='outer')
res2= pd.merge(left,right,left_index=True,right_index=True,how='inner')

print('8.\n')
print(res1)
print(res2)

#handle overlapping
boys= pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls= pd.DataFrame({'k':['K0','K0','K3'],'age':[4,5,6]})

res=pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='inner')

print(res)
