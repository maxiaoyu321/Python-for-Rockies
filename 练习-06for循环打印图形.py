#打印正三角形
'''
*
* *
* * *
* * * *
* * * * *
'''
#i控制行，j控制列
for i in range(1,6):
    print("* "*i,)
#第二种方法
print("##########")
for i in range(5):
    for j in range(i+1):
        print("* ",end="")
    print()
print("##########")

#打印空三角形
'''
*
* *
*   *
*     *
*       *
* * * * * *
'''
for i in range(6):
    for j in range(i+1):
        if i==0 or i==5:
            print("* ",end="")
            continue
        if j==0 or j==i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
print("##############")
#打印一个正三角形
'''
          *
         * *
        * * *
       * * * *
      * * * * * 
'''
for i in range(5):
    for j in range(5-i):
        print(" ",end="")
    print(" *"*(i+1),end="")
    print()
print("############")
#打印一个空的倒三角
'''
*******
 *   *
  * *
   *      
'''
for i in range(4):
    for j in range(7-i):
        if i==0:
            print("*",end="")
            continue
        if j==6-i or j==i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
print("##########")
#汉诺塔问题
'''
规则1，每次只能移动一个盘子
规则2，大盘子不能放到小盘子上边
'''
global n
def hanuo(n,a,b,c):
    if n==1:
        print(a,"-->",c)
        return None
    if n==2:
        print(a,"-->",b)
        print(a,"-->",c)
        print(b,"-->",c)
        return None
    hanuo(n-1,a,c,b)#将最后一个盘子从a转移到c，调用递归
    print(a,"-->",c)
    hanuo(n-1,b,a,c)#将b上的n-1个盘子，通过a转移到c上，调用递归


a = "A"
b = "B"
c = "C"
n = input("请输入盘子的数量：")
n = int(n)
print("您总共需要移动{}步".format(2**n-1))
print("步骤如下：")
hanuo(n,a,b,c)





