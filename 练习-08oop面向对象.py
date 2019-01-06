'''
建立第一个练习类
学生类
'''
class Student():
    name = None
    age = 18
    course = "python"
    def doingHomework(self):
        print("我正在做作业")
        return None
yueyue = Student()
print(yueyue.age)
print(yueyue.name)
yueyue.doingHomework()