# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/30 21:34
# 文件名称：class14.py
# 开发软件：PyCharm
from random import randint

class Die():
    def __init__(self):
        self.sides = 6

    def roll_die1(self):
        self.sides = randint(1,6)

    def roll_die2(self):
        self.sides = randint(1,10)

    def roll_die3(self):
        self.sides = randint(1,20)

die = Die()
print(die.sides)
die.roll_die1()
print(die.sides)
die.roll_die2()
print(die.sides)
die.roll_die3()
print(die.sides)
