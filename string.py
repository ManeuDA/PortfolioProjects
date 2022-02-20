#Strings

def first_and_last(message):
        if message[0]==message[-1]:
            return True
        return False

print(first_and_last("else"))       #True
print(first_and_last("toy"))        #False

pets = "Cats & Dogs"
print(pets.index("&"))          # anwser: 5
print(pets.index("s"))          #answer:3

# in keyword "in" to find out if substring is part of string
print("Dragons" in pets)        #False
print("Cats" in pets)           #True

#update of old email to new email
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@"+ old_domain)
        new_email = email[:index] +"@" + new_domain #update with new domain About the job


print("Mountains".upper())      #MOUNTAINS
print("Mountains".lower())      #mountains
print(" yes ".strip())      #Answer: yes  # Note: rstrip and lstrip also can be use to remove white space right or left

answer = "YES"
if answer.lower() == "yes":
    print("User said yes")          #User said yes

print("The number of times e occurs in this string is 4".count("e"))  # 4  #note : count # of substring "e" in strings
print("Forest".endswith("rest"))   # TRUE #note: true or false if the string endswith substring
print("Forest".isnumeric())     #FALSE # note: is the string numeric? true or false?
print("12345".isnumeric())      # TRUE # note: is the string numeric? here True
print(int("12345") + int("54321"))      #66666 #note change string numbers to integer
print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])) #This is a phrase joined by spaces
print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple","dots"]))
#This...is...a...phrase...joined...by...triple...dots
print("This is another example".split())    #['This', 'is', 'another', 'example']
print("list".split())   #['list']

#Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase
# received, in upper case. For example: "Universal Serial Bus" should return "USB";
# "local area network" should return "LAN”

def initials(phrase):
    phrase = (phrase)
    words = phrase.split()
    #return words
    initials = ""
    for word in words:
        initials += word[0].upper()
    return initials

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS


#name = input("Enter your name: ")
name = "Max"
number = len(name)*3
print("Hello {}, your lucky number is {}".format(name, number))
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))
# Hello Max, your lucky number is 9, # Your lucky number is 9, Max.

#{} placeholder can be filled with variables, then set the values by assigning values inside parameters in format
#Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam".
# For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".
def student_grade(name, grade):
    return "{} received {}% on the exam.".format(name,grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))
#Reed received 80% on the exam. Paige received 92% on the exam. Jesse received 85% on the exam.

#formating expression # 2 decimal points
price = 7.5
with_tax = price * 1.09
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
# Base price: $7.50. With Tax: $8.18
# Note: telling python to show different values than default.
# inside {} : seperate the field name .2f float number with 2 decimal after dot (.)

# formatting expression ">"  to align the text to the right
def to_celsius(x):
    return (x -32)*5/9

for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
#  0 F | -17.78 C
# 10 F | -12.22 C
# 20 F |  -6.67 C
# 30 F |  -1.11 C
# 40 F |   4.44 C
# 50 F |  10.00 C
# 60 F |  15.56 C
# 70 F |  21.11 C
# 80 F |  26.67 C
# 90 F |  32.22 C
#100 F |  37.78 C

# inside {} :>3 we want the number to be agined on the right total 3 spaces
#           :>6.2f number to be aligned on the right total 6 spaces, two decimal points float numbers

#String Reference Cheat Sheet
# In Python, there are a lot of things you can do with strings. In this cheat sheet, you’ll find the most
# common string operations and string methods.

#String operations
#len(string) Returns the length of the string
#for character in string Iterates over each character in the string
# if substring in string Checks whether the substring is part of the string
# string[i] Accesses the character at index i of the string, starting at zero
# string[i:j] Accesses the substring starting at index i, ending at index j-1.
# If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.

#String methods
#string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
#string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
#string.count(substring) Returns the number of times substring is present in the string
#string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
#string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
#string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
#string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
#delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter
#Check out the official documentation for all available String methods.
# https://docs.python.org/3/library/stdtypes.html#string-methods

#Formatting Strings Cheat Sheet

#Python offers different ways to format strings. In the video, we explained the format() method.
# In this reading, we'll highlight three different ways of formatting strings. For this course you only need to
# know the format() method. But on the internet, you might find any of the three, so it's a good idea to know that
# the others exist.

#Using the format() method
#The format method returns a copy of the string where the {} placeholders have been replaced with the values of the
# variables. These variables are converted to strings if they weren't strings already. Empty placeholders are replaced
# by the variables passed to format in the same order.

# "base string with {} placeholders".format(variables)

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)
''' Output
this is an example of using the format() method on a string
'''

#If the placeholders indicate a number, they’re replaced by the variable corresponding to that order (starting at zero).

# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)  # apple carrot banana

#If the placeholders indicate a field name, they’re replaced by the variable corresponding to that field name.
# This means that parameters to format need to be passed indicating the field name.

# "{var1} {var2}".format(var1=value1, var2=value2)
# "{:exp1} {:exp2}".format(value1, value2)

#If the placeholders include a colon, what comes after the colon is a formatting expression.
# See below for the expression reference. Official documentation for the format string syntax
#https://docs.python.org/3/library/string.html#formatstrings

# {:d} integer value
#'{:d}'.format(10.5) → '10'

#Formatting expressions
# Expr      Meaning                                     Example
#{:d}       integer value                               '{:d}'.format(10.5) → '10'
#'{:.2f}    floating point with that many decimals      '{:.2f}'.format(0.5) → '0.50'
#{:.2s}     string with that many characters            '{:.2s}'.format('Python') → 'Py'
#{:<6s}     string aligned to the left that many spaces '{:<6s}'.format('Py') → 'Py    '
#{:>6s}     string aligned to the right that many spaces'{:>6s}'.format('Py') → '    Py'
#{:^6s}     string centered in that many spaces         '{:^6s}'.format('Py') → '  Py  '

#check out the officil documentation for all available expressions:
#https://docs.python.org/3/library/string.html#format-specification-mini-language

#Question 1
# The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read
# from left to right or right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are
# words like kayak and radar, and phrases like "Never Odd or Even". Fill in the blanks in this function to return
# True if the passed string is a palindrome, False if not.

def is_palindrome(input_string):
    new_string = input_string.lower()
    reverse_string = ""
    for letter in new_string:
        reverse_string = new_string[-1]+new_string[1:-1]+new_string[0]
        #return reverse_string      #code above makes last letter to front while front goes to last
    if new_string == reverse_string:
        return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

#Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase
# "X miles equals Y km", with Y having only 1 decimal place. For example, convert_distance(12) should return
# "12 miles equals 19.2 km".
def convert_distance(miles):
	km = miles * 1.6
	result = "{} miles equals {:.1f} km".format(miles, km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

#Fill in the gaps in the nametag function so that it uses the format method to return first_name and the first initial
# of last_name followed by a period. For example, nametag("Jane", "Smith") should return "Jane S."
def nametag(first_name, last_name):
	name_first = first_name
	initial_last = last_name[0].upper()
	return "{} {}.".format(name_first,initial_last)

print(nametag("Jane", "Smith"))
    # Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
    # Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
    # Should display "Jean-Luc G."

#Question 5 The replace_ending function replaces the old string in a sentence with the new string, but only if the
# sentence ends with the old string. If there is more than one occurrence of the old string in the sentence, only the
# one at the end is replaced, not all of them. For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz,
# not xyzxyz or xyzabc. The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return
# abcabc (no changes made).

def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence
    if sentence.endswith(old):

		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the
		# end with the new string
        i = sentence.rsplit(old,1)
        new_sentence = new.join(i)
        return new_sentence
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"


