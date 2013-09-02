# -*- coding: utf-8 -*-

x = "There are %d types of people." % 10 # 声明 x 字符串
binary = "binary" # 声明 binary 字符串
do_not = "don't" # 声明 do_not 字符串
y = "Those who know %s and those who %s." % (binary, do_not) # 声明 y 字符串

print x # 打印 x 字符串
print y # 打印 y 字符串

print "I said: %r." % x # 打印
print "I also said: '%s'." % y # 打印

hilarious = False # 声明 hilarious
joke_evaluation = "Isn't that joke so funny?! %r" # 声明 joke_evaluation
print joke_evaluation % hilarious

w = "This is the left side of..." # 声明 w
e = "a string with a right side." # 声明 e

print w + e # 打印 e 和 w