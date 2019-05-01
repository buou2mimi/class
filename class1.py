# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/28 15:11
# 文件名称：class1.py
# 开发软件：PyCharm
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.type=cuisine_type

    def describe_restaurant(self):
        print("The restaurant's name is {} and its cuisine tpye is {}.".format(self.name.title(),self.type.title()))

    def open_restaurant(self):
        print("The restaurant is open!")

restaurant=Restaurant("quanjude","barbecue")
print(restaurant.name.title())
print(restaurant.type)
restaurant.describe_restaurant()
restaurant.open_restaurant()