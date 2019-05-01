# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/30 20:17
# 文件名称：my_electric_car.py
# 开发软件：PyCharm
from electric_car2 import ElectricCar

my_tesla = ElectricCar('tesla','model s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()