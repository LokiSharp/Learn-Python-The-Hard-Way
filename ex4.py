# -*- coding: utf-8 -*-

cars = 100 # 声明车的数量
space_in_a_car = 4.0 # 声明车内空间
drivers = 30 # 声明驾驶员数量
passengers = 90 # 声明乘客数量
cars_not_driven = cars - drivers # 计算无驾驶员的车
cars_driven = drivers # 声明被驾驶的车
carpool_capacity = cars_driven * space_in_a_car # 计算载客能力
average_passengers_per_car = passengers / cars_driven # 计算平均车内乘客数


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."