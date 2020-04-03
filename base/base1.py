# python 输出
apple = 1
appleFruit = 12+19
a, b, c = 1, 2, 3
print(apple)
print(appleFruit)
print(1, b, c)

# python while 循环
condition = 1
while condition < 10:
    print(condition)
    condition += condition

# Python for 循环
exampleList = [1, 2, 3, 4, 55, 6, 7]
for i in exampleList:
    print(i)

for i in range(1, 10):
    print(i)

    # 3为步长
for i in range(1, 10, 3):
    print(i)

# python条件判断
x, y, z = 1, 2, 3
if x < y:
    print("x is less than y")

if x < y < z:
    print("x is less than y,z is bigger than y.")

if x < y > z:
    print("x is less than y,z is bigger than y.")
else:
    print("text")

if x > 1:
    print("x>1")
elif x < 1:
    print("x<1")
else:
    print("x=1")

# python 函数定义
    # def:表示define
def function():
    a, b, c = 1, 2, 3
    print("This is a function")
    
def add(a,b):
    print('The result is', a+b)

add(a=2, b=5)

# python 默认参数（默认参数只能放在后面）
def car(color,band='camy',isSecondHand=True):
    print('color:', color,
          'band:', band,
          'isSecondHand:', isSecondHand)

car('RED')

# python 全局与局部变量
# global a：全局变量a指针指向新的内存
a = None
def changeGlobal():
    global a
    a = 20
    return a+200

print(a)
print(changeGlobal())
print(a)


