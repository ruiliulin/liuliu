# 11-3 雇员
class Employee():

    def __init__(self, f_name, l_name, yearly_salary):
        self.name = f_name +' ' + l_name
        self.yearly_salary = yearly_salary

    def give_raise(self, r=5000):
        self.yearly_salary += r
        return self.yearly_salary

