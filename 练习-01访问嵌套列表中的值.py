#定义一个列表，该列表中存在嵌套列表
movie = [
    ["钢铁侠一","钢铁侠二","钢铁侠三"],
    ["雷神一","雷神二","雷神三"],
    ["复仇者联盟一","复仇者联盟二"],
    "银河护卫队","绿巨人",
    ["美国队长","美国队长2"]]
#利用for循环打印列表中的元素
for each_flicks in movie:
    if isinstance(each_flicks,list):
        #判断列表元素是不是列表
        for new_flicks in each_flicks:
            print(new_flicks)
    else:
        print(each_flicks)
print("#################")
#删除列表中的最后一项
movie.pop()
print(movie)
print("#################")
#在列表结尾处中插入内容["银河护卫队1","银河护卫队2"]
movie.extend([["银河护卫队1","银河护卫队2"]])
print(movie)
print("###################")
#在列表的指定位置插入“复仇者联盟3”
movie.insert(2,"复仇者联盟3")
print(movie)
#在列表中移除指定的一项
movie.remove("复仇者联盟3")
print(movie)
#向访问列表中的列表的某个值
print(movie[2][1])
