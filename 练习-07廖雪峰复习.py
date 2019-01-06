#控制浮点型数据的位数
print("{0:.3f}".format(3.3*102))



#review .hanuo tower
def hanuo(n,a,b,c):
    if n==1:
        print(a,"==",c)
    if n==2:
        print(a,"==",b)
        print(a,"==",c)
        print(b,"==",c)
    else:
        hanuo(n-1,a,c,b)
        print(a,"==",c)
        hanuo(n-1,b,a,c)
n = 3
a = "a"
b = "b"
c = "c"
hanuo(n,a,b,c)


t = (1,2,3,4,5)
L = len(t)
print(L)

d = {"name":"maxiaoyu","age":26,"class":4}
print(d["name"])

dd = {k:v for k,v in d.items()}
print(dd)

for k in d.keys():
    print(k)

print(d.get("name","没有该元素"))
print(d.get("maxiaoyu","没有该元素"))

#使用指定的序列作为键
k1 = [k for k in range(1,5)]
d = dict.fromkeys(k1,["name","age","class","dress"])
print(d)

l = [1,2,3,4,56,66,777]
print(type(l))
s = set(l)

#打印圣诞树

for i in range(12):
    print(" "*(11-i)+'*'*(i*2+1))
print(" "*10+"|")

import random
height = 11
for i in range(height):
    print(' ' * (height - i), end='')
    for j in range((2 * i) + 1):
        if random.random() < 0.1:
            color = random.choice(['\033[1;31m', '\033[33m', '\033[1;34m'])
            print(color, end='')  # 彩灯
        else:
            print('\033[32m', end='')  # 绿色
        print('*', end='')
    print()
print((' ' * height) + '|')


import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

