def my_function():
    print("Hello from a function")

my_function()

 #parameters
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#default parameter value
def my_function(country = "Norway"):
    print ("i am from" + country)

my_function("Sweden")
my_function("india")
my_function()
my_function("Brazil")

 #passing a list as a parameter
def my_function(food):
    for x in food:
        print(x)

        fruits = ("apple", "banana", "cherry")
        my_function(fruits)

#this one is like your script with arvg

def print_two (*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that *args is actually pointless, we can just do this
def print_two_again (arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one argument
def print_one(arg1):
    print "arg1: %r" %(arg1)

#this one takes noarguments
def print_none():
    print "i got nothing"


print_two("zed", "shawn")
print_one("first!")
print_none()
