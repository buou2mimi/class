# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/30 20:48
# 文件名称：class11.py
# 开发软件：PyCharm
from class8 import User,Privileges,Admin

administrator = Admin('cai','xukun',19,'basketball')
administrator.privileges.show_privileges()