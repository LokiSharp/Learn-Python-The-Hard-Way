from sys import argv

cen = float(argv)

fah = 32.0 + cen * 1.8

print "%f Fahrenheit is %f Centigrade" % (fah, cen)
