# -*- coding: utf-8 -*-

from sys import argv #  从 sys 引入 argv

script, input_file = argv # 解包 argv

def print_all(f): # 定义 print_all 函数，功能是打印全部
    print f.read() # 读取 f

def rewind(f): # 定义 rewind 函数，功能是返回文件的头部
    f.seek(0) # 调用 seek 函数返回 f 的头部

def print_a_line(line_count, f): # 定义 print_a_line 函数，作用是打印一行
    print line_count, f.readline() # 打印 行计数器和行

current_file = open(input_file) # 打开文件

print "First let's print the whole file:\n" # 打印

print_all(current_file) # 调用 print_all 函数，打印整个 current_file

print "Now let's rewind, kind of like a tape." # 打印

rewind(current_file) 调用 rewind 函数，返回 current_file 的头部

print "Let's print three lines:" # 打印

current_line = 1 # 初始化行计数为 1
print_a_line(current_line, current_file) # 调用 print_a_line 函数，打印一行

current_line = current_line + 1 # 行计数 + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)