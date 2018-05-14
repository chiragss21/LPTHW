#imports a feature/module
from sys import argv

#takes the arguments given when running the script
#and puts them in two variables
script, filename = argv

#puts the file in variable txt after opening it
txt = open(filename)

print "Here's your file %r:" %filename
print txt.read()
txt.close()
"""
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
"""
