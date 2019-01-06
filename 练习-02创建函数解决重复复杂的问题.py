#举例，如果一个列表中存在多层嵌套的列表，打印列表中的所有内容
#for循环+if isinstance（name，list）,显然过于复杂
#创建一个嵌套列表列表
num = [1,2,3,
      [4,5,6,7],
      [7,8,9,[10,11,12,13,14,15]],
      ]
for each_item in num:
    if isinstance(each_item,list):
        for new_item in each_item:
            if isinstance(new_item,list):
                for deep_item in new_item:
                    print(deep_item)
            else:
                print(new_item)
    else:
        print(each_item)
print("另外一中的方法结果如下")