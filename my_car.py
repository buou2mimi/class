# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/30 20:13
# 文件名称：my_car.py
# 开发软件：PyCharm
from car2 import Car

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()