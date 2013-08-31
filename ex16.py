# -*- coding: utf-8 -*-

from sys import argv # 从 import 库中引入 argv

script, filename = argv # 给 filename 赋值为 argv

####----    打印    ----####
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
####----  EOF 打印  ----####

raw_input("? ") # 确认 

print "Opening the file..." # 打印
target = open(filename, 'w') # 以写入模式在 target 中打开名为 filename 的文件

#print "Truncating the file. Goodbye!" # 打印
#target.truncate # 清空 target

print "Now I'm going to ask you for three lines." # 打印

####----    输入    ----####
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
####----  EOF 输入  ----####

print "I'm going to write these to the file." # 打印

####----    写入    ----####
target.write("%s\n%s\n%s\n" % (line1,line2,line3))
####----  写入 EOF  ----####

print "And finally, we close it." # 打印
target.close() # 关闭 target