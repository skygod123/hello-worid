#!/usr/bin/python3
import sys

print("你好，世界");
# !/usr/bin/python3
# -*- coding: UTF-8 -*-
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']


"""as """

import sys; x = 'runoob'; sys.stdout.write(x + '\n')
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

input("\n\n按下 enter 键后退出。")

x = "a"
y = "b"
print(x, end=" ")
print(y, end=" ")



print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
var1 = 1
var2 = 10

str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0:])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[:-2])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if ('Rose' in student):
        print('Rose 在集合中')
else:
        print('Rose 不在集合中')
