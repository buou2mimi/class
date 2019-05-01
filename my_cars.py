# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/30 20:22
# 文件名称：my_cars.py
# 开发软件：PyCharm
from electric_car2 import Car,ElectricCar

my_beetle = Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())