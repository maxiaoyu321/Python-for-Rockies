#默认参数
def reg(name, age, gender="male"):
    if gender=="male":
        print("woshinansehng")
        print("wojiao{0},wojinina {1}".format(name,age))
    else:
        print("woshijvsheng")
        print("wojiao{0},wojinina {1}".format(name,age))
reg("xiaoming",18,"femal")
reg(18,"maxiaoyu")
#关键字参数


#练习：打印嵌套列表中所有的值
def print_lol(the_list,level=0):
    '''利用到的知识点有默认参数，for循环
    if判断语句、end=""，/转义字符
    :param the_list: 定义列表
    :param level: 嵌套列表的层级
    :return:
    '''
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,level+1)#如果我发现嵌套列表中某一个列表中还存在列表，那么就在执行一次上边的判断程序
        else:
            for tap_stop in range(level):
                print("有啥用\t",end="")
            print(each_item)

movie = [1,2,3,[4,5,6,[7,8,[9,10]]]]
print_lol(movie)





def num(the_list,indent=False,level=0):
   for each_item in the_list:
       if isinstance(each_item,tuple):
           num(each_item,indent,level+1)
       else:
           if indent:
               for tab_stop in range(level):
                   print("有啥用\t",end="")
               print(each_item)


list = [1,2,3,[4,5,6,[7,8,9]]]

num(list,indent=True)

help(print_lol)
print("#"*10)

#收集参数与收集关键字参数的练习
def stu(name,age,*args,first_lover="徐美丽",hobby="我喜欢打球",**kwargs):
    print("大家好，这是我的自我介绍")
    if first_lover == "徐美丽":
        print("我的名字是{0}，我今年{1}岁了，我的初恋是{2}".format(name,age,first_lover))
        if hobby == "我喜欢打球":
            print("我喜欢打球")
    for i in args:
        print(i)

    for k,v in kwargs:
        print(k,"....",v)

a = stu("mayunkun",19,"白雪纯",hobby="我喜欢打游戏")
b = stu("liuxiaofang",19,first_lover="shit",hobby="我喜欢打游戏")
print(b)

