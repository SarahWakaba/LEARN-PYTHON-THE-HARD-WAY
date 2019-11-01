i = 0
numbers = []

while i < 6:
    print "At the top i is %d " % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d " % i

print "The numbers: "

for num in numbers:
    print num


#Accessing elements of lists
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
1. The animal at 1
2. The 3rd animal
3. The 1st animal
4. The anomal at 3
5. The 5th animal
6. The animal at 2
7. The 6th animal
8. The animal at 4
