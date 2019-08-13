"""一组关于管理员信息和权限的类"""

from user_2 import User

class Privileges():

    def __init__(self):
        """管理员的特权待遇"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """展示管理员的特权待遇"""
        print('管理员权限为 ' + str(self.privileges))


class Admin(User):

    def __init__(self, first_name, last_name, age, sex, addr):
        """管理员所具有的属性和特权"""
        super().__init__(first_name, last_name, age, sex, addr)
        self.privileges = Privileges()
