print "You enter a room with two doors. Do you go through door #1 or door #2?"
door = raw_input("> ")


if door == "1":
     print "There is a giant bear here eating a cheese cake. What do you do?"
     print "1. Take the cake,"
     print "2. scream at the bear."

     bear = raw_input(">")

     if bear == "1":
         print "The bear eats your face off. Good job!"
     elif bear == "2":
        print "The bear eats your legs off. Good job!"
     else:
        print "Well, doing %s is probably better. Bear runs away." % bear
elif door == "2":
    print "You stare into the endless abyss at cthuhlu retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothspines."
    print "3. U nderstanding revolvers yelling melodies."

    insanity = raw_input(">")
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job1"

else:
    print "You stubble around and fallon a knife and die. Good job!"
