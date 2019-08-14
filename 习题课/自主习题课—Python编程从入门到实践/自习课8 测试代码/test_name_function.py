
import unittest

from name_function import get_formatted_name

# 创建一个用于测试函数的类
class NamesTestCase(unittest.TestCase):
    '''测试name_function.py'''

    def test_first_last_name(self):
        '''能够正确处理像Liu Dana这样的姓名吗？'''
        formatted_name = get_formatted_name('liu', 'dana')
        self.assertEqual(formatted_name, 'Liu Dana')

    def test_first_last_middle_name(self):
        '''能够正确处理像Liu Da Na这样的姓名吗？'''
        formatted_name = get_formatted_name('liu', 'na', 'da')
        self.assertEqual(formatted_name, "Liu Da Na")


if __name__ == '__main__':
    unittest.main()