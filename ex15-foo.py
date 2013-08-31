print ("gave me a filename")
filename = raw_input("> ")
txt = open(filename)


print ("Here is you file!")
print txt.read()

txt.close()