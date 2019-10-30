print "hello again"
print "i like typing this"
print "this is fun"
print "yay! Printing"
print "i'd much rather you 'not'."
print 'i "said" do not touch this'
# a comment this is so you can run your program later
# Anything after the # is ignored by python.
print "i could have a code like this" # and the project after this is ignored
# You can also use a comment to "disable" or comment out a piece of code
print "this wont run."

#Numbers and maths
print "i will now count my chickens."
print "hens", 25 + 30 / 6
print "roosters", 100 - 25 % 4
print "now i will count my eggs"
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print "is it true that 3 + 2 < 5 - 7?"
print "3 + 2 > 5 -7"
print "what is 3 + 2?" , 3 + 2
print "what is 5 - 7?" , 5 - 7
print "oh, thats why it's false. "
print "How about some more"
print "is it greater?", 5 > -2
print "is it greater or equal to?", 5 <= -2

#variables and names
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We need to put about", average_passengers_per_car, "in each car."

#More variables and Printing
my_name = 'zed A. Shawn'
my_age = 35 # not a lie
my_height = 75 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy" % my_weight
print "Actually thats not too heavy"
print "He's got %s eyes and %s hair." % (my_eyes , my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
my_age, my_height, my_weight, my_age + my_height + my_weight)

#Strings and texts
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
print "i said: %r." % x
print "i also said: '%s'." % y

hilarious = "false"
joke_evaluation = "isn't that joke so funny?! %r"
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side"
print w + e

#MORE PRINTING
print"Its fleece was white as %s." % 'snow'
print"And everywhere that Mary went."
# what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

#PRINTING PRINTING
formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "Two", "Three", "Four")
print formatter % ("True", "False", "False", "True")
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)
#Here is some new stuff.Remember type it exactly
days = "mon tue wed thur fri sat sun"
months = "Jan\n Feb\n march\n april\n may\n june\n july\n august\n september\n october\n"
print "Here are the days: ", days
print "Here are the months: ", months
print """
There is something going on Here.
with the three double quotes.
we will be able to type as much as we like.
"""
#Escaping double quotes
"I am 6'2\" tall." #escape double quotes inside Strings
tabby_cat = "\ti am tabbed in."
persian_cat = "I am split\non a line"
blackslash_cat = "I'm \\ a \\ cat"

fat_cat = """
i'll do a list:
 \t* cat food
 \* fishies
 \*catnib\n\t* grass
 """
print tabby_cat
print persian_cat
print blackslash_cat
print fat_cat
