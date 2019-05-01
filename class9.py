# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/30 19:51
# 文件名称：class9.py
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

class Battery():
    """一次模拟电动车电瓶的简单尝试"""
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size=battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a {}-kWh battery.".format(self.battery_size))

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        massage = "Thie car can go approximately {} miles on a full charge.".format(range)
        print(massage)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性，再初始化电动车特有的属性"""
        super().__init__(make,model,year)
        self.battery=Battery()

my_tesla = ElectricCar('tesla','model s',2016)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()