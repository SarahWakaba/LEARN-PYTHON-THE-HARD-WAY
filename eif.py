people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We canno' decide"


if buses > cars:
    print "That too many buses."
elif buses < cars:
    print "May be we would take the buses."
else:
    print "We still cant decide."

if people > buses:
    print "Alright lets just take the buses."
else:
    print "Fine let's just stay at home then."
