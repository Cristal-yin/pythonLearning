# 面向对象
# 有意义的面向对象的代码
# 类 = 面向对象
# 类、对象
# 实例化
# 类的最基本的作用就是封装
class Student():
    # 一个班级里所有学生的总数
    sum = 0
    name = 'rocky' 
    age = 0
    # 行为 与 特征
    def __init__(self,name,age):
        # 初始化对象的属性
        self.name = name
        self.age = age
        self.__score = 0
        #构造函数 定义对象的时候会自动调用
        # print('Student')
        self.__class__.sum += 1
        print('当前学生数目:'+str(self.__class__.sum))
        #构造函数不能返回None之外的值
        
    def marking(self,score):
        if score < 0:
            return '不能打负分'
        self.__score = score
        print(self.name+'分数'+str(self.__score))
    def do_homework(self):
        self.do_english_homework()
        print('homework')
        
        
    def  do_english_homework(self):
        print('do_english_homework')
        
    @classmethod
    def sum_plus(cls):
        cls.sum += 1
        print(cls.sum)
        
        
    @staticmethod
    def add(x,y):
        print()
        
        
student1 = Student('Cristal',18)

result = student1.marking(-1)
if(result):
    print(result)
    
student1.__score = 90
student2 = Student('Rocky',19)
print(student1.__score)
# 为什么在这里调用私有的成员变量不会报错的？
# 对student1新添加了一个__score变量 不是原来的了
# 其实正常来说是不可以访问的 也不可以再定义
print(student1.__dict__)
print(student2.__dict__)
# print(student2._Student__score) 自觉点不去读
# student1.sum_plus()
# student1.do_homework()
# print(student1.name)
# print(Student.name)
# class Printer():
#         def print_file(self):
#             print('name:' + self.name)
#             print('age:' + str(self.age))