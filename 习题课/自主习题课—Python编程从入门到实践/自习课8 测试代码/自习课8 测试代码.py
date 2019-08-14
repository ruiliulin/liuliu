# Python编程——从入门到实践（11章）
# -1 测试函数
# 初始案例见name_function.py和names.py
# 使用模块unittest进行测试
# 首先导入模块unittest和要测试的函数get_formatted_name
"""
import unittest
from name_function import get_formatted_name

# 创建一个用于测试函数的类
class TestCase(unittest.TestCase):
    '''测试name_function.py'''

    def test_first_last_name(self):
        '''能够正确处理向Liu Dana这样的姓名吗？'''
        formatted_name = get_formatted_name('liu', 'dana')
        self.assertEqual(formatted_name, 'Liu Dana')

    def test_first_last_middle_name(self):
        '''能够正确处理像Liu Da Na这样的姓名吗？'''
        formatted_name = get_formatted_name('liu', 'na', 'da')
        self.assertEqual(formatted_name, "Liu Da Na")

# 测试代码
if __name__ == '__main__':
    unittest.main()
"""


# -2 测试类
# 6个常用的断言方法
# assertEqual(a, b)             核实a == b
# assertNotEqual(a, b)          核实a != b
# assertTrue(x)                 核实x为True
# assertFalse(x)                核实x为False
# assertIn(item, list)          核实item在list中
# assertNotIn(item, list)       核实item不在list中
# setUp()