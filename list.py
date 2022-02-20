#Lists Defined
# Lists in Python are defined using square brackets, with the elements stored in the list separated by commas:
# list = ["This", "is", "a", "list"]. You can use len() function to return the number of elements in a list: len(list)
# would return 4. You can also use the in keyword to check if a list contains a certain element. If the element is
# present, it will return a True boolean. If the element is not found in the list, it will return False. For example,
# "This" in list would return True in our example. Similar to strings, lists can also use indexing to access specific
# elements in a list based on their position. You can access the first element in a list by doing list[0], which would
# allow you to access the string "This".

#In Python, lists and strings are quite similar. They’re both examples of sequences of data. Sequences have similar
# properties, like (1) being able to iterate over them using for loops; (2) support indexing; (3) using the len function
# to find the length of the sequence; (4) using the plus operator + in order to concatenate; and (5) using the in
# keyword to check if the sequence contains a value. Understanding these concepts allows you to apply them to other
# sequence types as well.

#Modifying Lists
# While lists and strings are both sequences, a big difference between them is that lists are mutable.
# This means that the contents of the list can be changed, unlike strings, which are immutable. You can add,
# remove, or modify elements in a list.

# You can add elements to the end of a list using the append method. You call this method on a list using dot notation,
# and pass in the element to be added as a parameter. For example, list.append("New data") would add the string
# "New data" to the end of the list called list.

# If you want to add an element to a list in a specific position, you can use the method insert. The method takes
# two parameters: the first specifies the index in the list, and the second is the element to be added to the list.
# So list.insert(0, "New data") would add the string "New data" to the front of the list. This wouldn't overwrite the
# existing element at the start of the list. It would just shift all the other elements by one.
# If you specify an index that’s larger than the length of the list, the element will simply be added to the
# end of the list.

#You can remove elements from the list using the remove method. This method takes an element as a parameter, and removes
# the first occurrence of the element. If the element isn’t found in the list, you’ll get a ValueError error explaining
# that the element was not found in the list.

#You can also remove elements from a list using the pop method. This method differs from the remove method in that it
# takes an index as a parameter, and returns the element that was removed. This can be useful if you don't know what
# the value is, but you know where it’s located. This can also be useful when you need to access the data and also want
# to remove it from the list.

#Finally, you can change an element in a list by using indexing to overwrite the value stored at the specified index.
# For example, you can enter list[0] = "Old data" to overwrite the first element in a list with the new string
# "Old data".

x = ["Now", "old", "4", "Excellent!"]
print(type(x))          #<class 'list'>
print(len(x))           #4 how many elements in the list
print( "old" in x)      #true
print("me" in x)        #false
print(x[0])             #now
print(x[1:3])           #['old', '4']

#Using the "split" string method from the preceding lesson, complete the get_word function to return the {n}th word
# from a passed sentence. For example, get_word("This is a lesson about lists", 4) should return "lesson", which is
# the 4th word in this sentence. Hint: remember that list indexes start at 0, not 1.

def get_word(sentence, n):
    sentence_list = sentence.split()
    if n >=0 and  n <= len(sentence_list):
        index = sentence_list[n - 1]
        return index
    else:
        return "List Index out of range"


print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing # note TRACEBACK ERROR Code above is not 100% ok

#append (add at the end), insert(using index as first parameter), remove (remove), pop(index#) - remove the index#
#assign index# with new element

fruits = ["Pineapple", "Banana", "Apple", "Pear"]
fruits.append("Kiwi")
print(fruits)       #['Pineapple', 'Banana', 'Apple', 'Pear', 'Kiwi']
fruits.insert(0,"Orange")           #index as first parameter, element as a second parameter
print(fruits)       #['Orange', 'Pineapples', 'Banana', 'Apple', 'Pear', 'Kiwi']
fruits.insert(25,"Peach")       #what happend when the index is larger than length
print(fruits)  #['Orange', 'Pineapple', 'Banana', 'Apple', 'Pear', 'Kiwi', 'Peach']     #element just added to the end
fruits.remove("Pear")
print(fruits)       #['Orange', 'Pineapple', 'Banana', 'Apple', 'Kiwi', 'Peach']
fruits.pop(3)       #remove index 3
print(fruits)       #['Orange', 'Pineapple', 'Banana', 'Kiwi', 'Peach']
fruits[2] = "Strawberry"    #assign index# with new element
print(fruits)       #['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']


#The skip_elements function returns a list containing every other element from an input list, starting with the first
# element. Complete this function to do that, using the for loop to iterate through the input list.

def skip_elements(elements):
    second_elements = []
    for index in range(0, len(elements), 2):
        second_elements.append(elements[index])
    return second_elements


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

#Question 1
#Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we
# would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the
# code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
newfilenames = []
# using as many lines of code as your chosen method requires.
for file in filenames:
    newfile=file.replace(".hpp", ".h")
    newfilenames.append(newfile)

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


#Question 2
# Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving
# the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.

def pig_latin(text):
    say = ""
    words = text.split()    # Separate the text into words
    for word in words:
        say += word[1:] + word[0] + 'ay'+ ' '  # Create the pig latin word and add it to the list
    return say # Turn the list back into a phrase

print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"

# Question 3
#The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and
# execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing
# each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string
# using the letters r, w, and x or - when the permission is not granted.
#For example:
#640 is read/write for the owner, read for the group, and no permissions for the others;
# converted to a string, it would be: "rw-r-----"
#755 is read/write/execute for the owner, and read/execute for group and others; converted to a string,
# it would be: "rwxr-xr-x"
#Fill in the blanks to make the code convert a permission in octal format into a string format.

def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for number in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if  number >= value:
                result += letter
                number -= value
            else:
                result += '-'
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------

# Question 5
# The group_list function accepts a group name and a list of members, and returns a string with the format: group_name:
# member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this
# function to do that.

def group_list(group, users):
    members = ','.join(users)
    return group +':'+ members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

#Question 6
#The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints
# the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"),
# ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is
# 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function
# to do that.

def guest_list(guests):
	for name, age, job in guests:
		print("{} is {} years old and works as {}".format(name, age, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])


#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""