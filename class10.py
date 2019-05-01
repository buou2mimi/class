# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/30 20:43
# 文件名称：class10.py
# 开发软件：PyCharm
from class1 import Restaurant

restaurant=Restaurant("quanjude","barbecue")
print(restaurant.name.title())
print(restaurant.type)
restaurant.describe_restaurant()
restaurant.open_restaurant()