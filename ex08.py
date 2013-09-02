# -*- coding: utf-8 -*-

formatter = "%r %r %r %r" # 声明 formatter

print formatter % (1, 2, 3, 4) # 打印数值
print formatter % ("one", "two", "three", "four") # 打印 字符串
print formatter % (True, False, False, True) # 打印布尔值
print formatter % (formatter, formatter, formatter, formatter) #打印变量
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
) #打印长字符串