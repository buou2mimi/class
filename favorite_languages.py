# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/30 20:59
# 文件名称：favorite_languages.py
# 开发软件：PyCharm
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name,language in favorite_languages.items():
    print("{}'s favorite language is {}.".format(name.title(),language.title()))
    