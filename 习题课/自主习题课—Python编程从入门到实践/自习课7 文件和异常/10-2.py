# C语言学习笔记
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for l in lines:
    print(l.rstrip().replace("Python", "C"))

