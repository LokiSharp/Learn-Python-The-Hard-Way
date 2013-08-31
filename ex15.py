# -*- coding: utf-8 -*-

from sys import argv # 从 sys 库中引入 argv

script, filename = argv # 声明 filename 为 argv

txt = open(filename) # 使用 open 命令给 txt 赋值为 filename 文件

print "Here's your file %r:" % filename # 打印
print txt.read() # 在 txt 上调用 read 函数

txt.close()

####----    再一次读取文件    ----####
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()
####----        EOF         ----####