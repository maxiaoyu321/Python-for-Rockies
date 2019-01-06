def num(the_list,indent=False,level=0):
   for each_item in the_list:
       if isinstance(each_item,list):
           num(each_item,indent,level+1)
       else:
           if indent:
               for tab_stop in range(level):
                   print("有啥用\t",end="")
               print(each_item)


list_1 = [1,2,3,[4,5,6,[7,8,9]]]

num(list_1,indent=True)