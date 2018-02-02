name = 'Zed A. Shaw'
age = 35 # not a lie

height = 74 # inches
weight = 180 # lbs
height_in_cm = height/0.393701
weight_in_kgs = weight/2.20462
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height_in_cm
print "He's %d pounds heavy." % weight_in_kgs
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and, %d I get %d." %(
  age, height_in_cm, weight_in_kgs, age + height_in_cm + weight_in_kgs)
