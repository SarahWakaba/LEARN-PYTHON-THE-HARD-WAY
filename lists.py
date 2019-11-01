the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this kind of for loop goes through a list
for number in the_count:
    print "This is count %d" % number

#same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit


#also we can go through mixed lists too
#notice we have tp use %r since we do not know whats in it
for i in change:
    print "I got %r" % i

#we can also build lists first starting with an empty one
elements = []

#then use the range function to do 0 to 20 counts
for i in range (0, 6):
    print "Adding %d to the list," % i
    #Append is a function that lists understand elements.append (i)

#now we can print them out too
for i in elements:
    print "Elements was: %d " % i

#Doing things to lists
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

    while len(stuff) != 10:
        next_one = more_stuff.pop()
        print "Adding: ", next_one
        stuff.append(next_one)
        print "There's %d items now." % len(stuff)

print "There we go: ", stuff
print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print   stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!
