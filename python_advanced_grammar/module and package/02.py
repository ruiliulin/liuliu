# 借助于importlib包可以实现导入以数字开头的模块名称
import importlib

# 相当于导入了一个叫01的模块并把它赋值给了tuling
tuling = importlib.import_module('03')

stu = tuling.Student()
tuling.sayhello()