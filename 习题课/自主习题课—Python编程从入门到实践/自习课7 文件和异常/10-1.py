# Python学习笔记
filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

with open(filename) as file_object:
    for l in file_object:
        print(l.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()
print(lines)
for l in lines:
    print(l.rstrip())