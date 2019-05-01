# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/28 20:52
# 文件名称：class4.py
# 开发软件：PyCharm
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.type=cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name is {} and its cuisine tpye is {}.".format(self.name.title(),self.type.title()))

    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_served(self,number):
        self.number_served=number

    def increment_number_served(self,increase):
        self.number_served+=increase

restaurant=Restaurant("haidilao","hot pot")

restaurant.number_served=23
print("{} people in the restaurant".format(restaurant.number_served))

restaurant.set_number_served(50)
print("{} people in the restaurant".format(restaurant.number_served))

restaurant.increment_number_served(10)
print("{} people in the restaurant".format(restaurant.number_served))

