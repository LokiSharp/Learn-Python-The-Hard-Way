# ﹣*- codeing: utf-8 -*-

def cheese_and_crackers(cheese_count, boxes_of_crackers): ＃ 函数
####----    打印    ----####
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
####----  打印 EOF  ----####

print "We can just give the function numbers directly:" # 以数值参数调用函数
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:" # 以变量方式调用函数
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:" # 以数值计算方式调用函数
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:" # 以数值与变量计算方式调用函数
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)