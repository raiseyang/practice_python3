"""
https://docs.python.org/3/library/os.path.html

在 Python 中， 读写文件有 3 个步骤：
1． 调用 open()函数， 返回一个 File 对象。
2．调用 File 对象的 read()或 write()方法。
3．调用 File 对象的 close()方法，关闭该文件。
"""
import os

path = os.path.join('C:', 'windows')
print(path)  # C:windows

# 创建文件夹
os.mkdir(path)

print(os.getcwd())  # 当前工作目录
# os.chdir('C:')  # 切换工作目录
print(os.getcwd())  # C:\

# os.makedirs('C:\\py_test_make\\second')  # 创建目录

print(os.path.abspath('.'))

path = 'C:/aa'
print(os.path.basename(path))  # 文件名或文件夹名称 aa
print(os.path.dirname(path))  # 父目录名称 C:/
print(os.path.split(path))  # ('C:/', 'aa')

print(os.path.sep)  # '\'

print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))  # 文件大小
# print(os.listdir('C:\\Windows\\System32'))

print(os.path.exists('C:'))  # True
print(os.path.isdir('C:'))  # True

file = open('C:\\kms10.log')
print(type(file))  # <class '_io.TextIOWrapper'>

content = file.read()  # 读取文件
# print(content)
content = file.readlines()  # 读取每行

# baconFile = open('a.txt', 'w')  # 写模式打开文件
# baconFile.write('\nHello world!\n')
with open('a.txt','w') as file:
    file.write('\nHello world!\n')

baconFile = open('a.txt', 'r')  # 读文件
print(baconFile.read())

with open('a.txt', 'r') as file:  # with 语法读取file
    print('with:', type(file))
    print('with content:', file.read())
