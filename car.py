# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/28 20:00
# 文件名称：car.py
# 开发软件：PyCharm
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())