"""一个关于用户信息的类"""

class User():

    def __init__(self, first_name, last_name, age, sex, addr):
        """初始化用户的属性"""
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.sex = sex
        self.addr = addr
        self.login_attempts = 0

    def describe_u(self):
        """描述用户的基本属性"""
        print('用户的姓名是{} {}'.format(self.fname.title(), self.lname))
        print('用户年龄：' + str(self.age))
        print('用户性别：' + self.sex)
        print('用户地址：' + self.addr)

    def greet_u(self):
        """打印一条问候语"""
        print('来自{}的{} {}{}士，见到你很高兴'.format(self.addr, \
                self.fname.title(), self.lname, self.sex))

    def increment_login_attempts(self):
        """打印用户的登录次数"""
        self.login_attempts += 1
        print("访问次数：" + str(self.login_attempts))

    def reset_login_attempts(self):
        """初始化用户的登录次数"""
        self.login_attempts = 0

