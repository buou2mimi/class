# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/28 21:08
# 文件名称：class5.py
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


user1 = User("cai", "xukun", 19, "basketball")
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)