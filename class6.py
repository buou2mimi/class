# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/30 17:02
# 文件名称：class6.py
# 开发软件：PyCharm
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.type=cuisine_type

    def describe_restaurant(self):
        print("The restaurant's name is {} and its cuisine tpye is {}.".format(self.name.title(),self.type.title()))

    def open_restaurant(self):
        print("The restaurant is open!")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['strawberry','blueberry','banana','watermelon']

    def show_flavors(self):
        print("Our shop has the following flavors of ice cream:")
        for flavor in self.flavors:
            print("\t{}".format(flavor.title()))

ice_cream_shop = IceCreamStand('Häagen-Dazs','ice cream')
ice_cream_shop.describe_restaurant()
ice_cream_shop.open_restaurant()
ice_cream_shop.show_flavors()

