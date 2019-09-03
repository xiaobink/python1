class Student:
    def __init__(self, name, job=None, time=0.00, time_effective=0.00): 
        self.name = name
        self.job = job
        self.time = time
        self.time_effective = time_effective

    def count_time(self, hour, rate):
        self.time += hour
        self.time_effective += hour * rate


# 完成子类的定制（包括初始化方法和count_time函数）
class Programmer(Student):
    def __init__(self,name):       #先把要重新赋值以及未赋值的参数写下来，默认参数可不写
        Student.__init__(self,name,job='programmer',time=0.00, time_effective=0.0)
        #将父类的初始化复制下来
        
    def count_time(self,hour,rate=1): #先把要重新赋值以及未赋值的参数写下来，默认参数可不写
        Student.count_time(self,hour,rate) #将父类的方法以及对应的参数复制下来
        


# 通过两个实例，完成子类和父类的对比
student1 = Student('韩梅梅')    #对实例调用父类
student2 = Programmer('李雷')   #对实例调用子类
print(student1.job)
print(student2.job)
student1.count_time(10,0.8)  #对方法中的参数进行赋值
student2.count_time(10)      #对方法中的参数进行赋值
print(student1.time_effective)   #打印出需要的参数值
print(student2.time_effective)   #打印出需要的参数值
