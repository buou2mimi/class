# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/30 17:27
# 文件名称：class7.py
# 开发软件：PyCharm
class User():
    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        print("The user's information :\n\tfirst name:{}\n\tlast name:{}\n\tage:{}\n\thobby:{}"
              .format(self.first_name.title(), self.last_name.title(), self.age, self.hobby.title()))

    def greet_user(self):
        print("Hello,{} {}!".format(self.first_name.title(), self.last_name.title()))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self,first_name,last_name,age,hobby):
        super().__init__(first_name,last_name,age,hobby)
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        print("Here are the administrator's privileges:")
        for privilege in self.privileges:
            print("\t{}".format(privilege.title()))

administrator = Admin('cai','xukun',19,'basketball')
administrator.describe_user()
administrator.greet_user()
administrator.show_privileges()
