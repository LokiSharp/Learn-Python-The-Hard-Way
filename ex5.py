name = 'Sharloki Wang'
age = 18
height = 185 # centimeter
weight = 180 # kilogram
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d centimeter tall." % height
print "He's %d kilograms heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get is exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
