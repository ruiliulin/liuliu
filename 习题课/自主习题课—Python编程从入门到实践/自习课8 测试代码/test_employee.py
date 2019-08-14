# 11-3 雇员
import unittest
from employee import Employee

class TestGiveRaise(unittest.TestCase):

    def setUp(self):
        self.ldn = Employee('liu', "dana", 1000000)

    def test_give_default_raise(self):
        self.ldn.give_raise()
        self.assertEqual(self.ldn.yearly_salary, 1005000)

    def test_give_cuntom_raise(self):
        self.ldn.give_raise(20000)
        self.assertEqual(self.ldn.yearly_salary, 1020000)

if __name__ == '__main__':
    unittest.main()