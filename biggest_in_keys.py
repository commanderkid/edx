#biggest
#Consider the following sequence of expressions:
animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['dog', 'donkey', 'dingo']}
#We want to write some simple procedures that work on dictionaries to return information.

#This time, write a procedure, called biggest, which returns the key corresponding to
#the entry with the largest number of values associated with it.
#If there is more than one such entry, return any one of the matching keys.

c, a = None, 0
for i in animals:
    if len(animals[i]) > a:
        a = len(animals[i])
        c = i
print(c)
