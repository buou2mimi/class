# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/28 14:35
# 文件名称：dog.py
# 开发软件：PyCharm
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name=name
        self.age=age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

my_dog=Dog('willie',6)
print("My dog's name is {}.".format(my_dog.name.title()))
print("My dog is {} years old.".format(str(my_dog.age)))
my_dog.sit()
my_dog.roll_over()

your_dog=Dog('lucy',3)
print("\nYour dog's name is {}.".format(your_dog.name.title()))
print("Your dog is {} years old.".format(str(your_dog.age)))
your_dog.sit()
your_dog.roll_over()