#斐波那契额数列
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib(n - 1)+fib(n - 2)
print(fib(4))

#汉诺塔问题
def hno(n):
    return 2**n - 1
print(hno(65))

#汉诺塔问题2
'''
f(k) = f(k-1)*2-1
'''
def hannuo(k):
    if k==1:
        return 1
    if k==2:
        return 3
    else:
        return 2*hannuo(k-1)-1
print(hannuo(65))

#数列的切片取值练习
l1=[1,2,3,4,5,6,7,8,9,10]
print(l1[5])
print(l1[1:10:2])
print(l1[-1:-6:-1])
l1.insert(1,888)
print(l1)


