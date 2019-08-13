"""一个表示餐馆的类"""

class Restaurant():

    def __init__(self, r_name, r_type):
        """初始化餐馆的名字，类型，访问人数初始设置为0"""
        self.name = r_name
        self.type = r_type
        self.number_served = 0

    def describe_r(self):
        """餐馆的基本内容(属性)"""
        print('餐馆的名字是：' + self.name.title())
        print(self.name.title() + '的类型是：' + self.type)

    def open_r(self):
        """餐馆营业中"""
        print(self.name + "正在营业中。。。。。。")

    def p_r(self):
        """打印总的就餐人数"""
        print("就餐人数是：" + str(self.number_served))

    def set_num_served(self, n):
        """确认就餐人数"""
        self.number_served = n

    def increment_num_served(self, l):
        """确认餐馆每天的就餐人数，递增到总的人数"""
        self.number_served += l
