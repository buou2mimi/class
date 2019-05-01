# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/28 21:29
# 文件名称：electric_car.py
# 开发软件：PyCharm
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has {} miles on it.".format(str(self.odometer_reading)))

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class ElectricCar(Car):
        """电动汽车的独特之处"""
        def __init__(self,make,model,year):
            """初始化父类的属性"""
            super().__init__(make,model,year)
            self.battery_size=70

        def describe_battery(self):
            """打印一条描述电瓶容量的信息"""
            print("This car has a {}-kWh battery.".format(self.battery_size))


my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()