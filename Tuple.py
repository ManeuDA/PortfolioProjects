#Lists and Tuples Operations Cheat Sheet
#Lists and tuples are both sequences, so they share a number of sequence operations. But, because lists are mutable,
# there are also a number of methods specific just to lists. This cheat sheet gives you a run down of the common
# operations first, and the list-specific operations second.

#Common sequence operations

# len(sequence) Returns the length of the sequence
# for element in sequence Iterates over each element in the sequence
# if element in sequence Checks whether the element is part of the sequence

# sequence[i] Accesses the element at index i of the sequence, starting at zero
# sequence[i:j] Accesses a slice starting at index i, ending at index j-1. If i is omitted, it's 0 by default.
# If j is omitted, it's len(sequence) by default.

# for index, element in enumerate(sequence) Iterates over both the indexes and the elements in the sequence
# at the same time

# Check out the official documentation for sequence operations.

# List-specific operations and methods
# list[i] = x Replaces the element at index i with x
# list.append(x) Inserts x at the end of the list
# list.insert(i, x) Inserts x at index i
# list.pop(i) Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.
# list.remove(x) Removes the first occurrence of x in the list
# list.sort() Sorts the items in the list
# list.reverse() Reverses the order of items of the list
# ist.clear() Removes all the items of the list
# list.copy() Creates a copy of the list
# list.extend(other_list) Appends all the elements of other_list at the end of list

# Most of these methods come from the fact that lists are mutable sequences. For more info, see the official
# documentation for mutable sequences and the list specific documentation.

# List comprehension
# [expression for variable in sequence] Creates a new list based on the given sequence. Each element is the
# result of the given expression.

# [expression for variable in sequence if condition] Creates a new list based on the given sequence.
# Each element is the result of the given expression; elements only get added if the condition is true.


# Tuples: The position of the elements inside the tuple have meaning.
# advantage of Tuples: we can unpack them. Since the position does not change, we know what it represents.

#Tuples
# As we mentioned earlier, strings and lists are both examples of sequences. Strings are sequences of characters,
# and are immutable. Lists are sequences of elements of any data type, and are mutable. The third sequence
# type is the tuple. Tuples are like lists, since they can contain elements of any data type. But unlike lists,
# tuples are immutable. They’re specified using parentheses instead of square brackets.

# You might be wondering why tuples are a thing, given how similar they are to lists. Tuples can be useful when
# we need to ensure that an element is in a certain position and will not change. Since lists are mutable,
# the order of the elements can be changed on us. Since the order of the elements in a tuple can't be changed,
# the position of the element in a tuple can have meaning. A good example of this is when a function returns multiple
# values. In this case, what gets returned is a tuple, with the return values as elements in the tuple.
# The order of the returned values is important, and a tuple ensures that the order isn’t going to change.
# Storing the elements of a tuple in separate variables is called unpacking. This allows you to take multiple
# returned values from a function and store each value in its own variable.

#Tuple of three elements
def converts_seconds(seconds):
    hours = seconds//3600
    minutes = (seconds - hours*3600)//60
    remaining_seconds = seconds - hours*3600 - minutes *60
    return hours, minutes, remaining_seconds

result = converts_seconds(5000)
print(type(result))             #answer: <class 'tuple'>
print(result)           #(1, 23, 20)

# Unpacking Tuples:
hours, minutes, seconds = result
print(hours, minutes, seconds)          #1 23 20

# or
hours, minutes, seconds = converts_seconds(1000)
print(hours, minutes, seconds)          #0 16 40

#Let's use tuples to store information about a file: its name, its type and its size in bytes.
# Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.
def file_size(file_info):
	name, type, size = file_info
	return("{:.2f}".format(size/ 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21


#Iterating over lists and Tuples
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)                #give total length of list of animals

print("Total characters:{}, Average length: {}".format(chars, chars/len(animals)))
#Total characters:22, Average length: 5.5

# enumerate function: to know index of elements while going through list
winners = ["Ashliey", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))       #1 - Ashliey, 2 - Dylan, 3 - Reese


#Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to
# return every other element from the list, this time using the enumerate function to check if an element is
# on an even position or an odd position.
def skip_elements(elements):
    second_elements = []
    for index, element in enumerate(elements):
        if index == 0:
            second_elements.append(element)
        elif (index % 2) == 0:
            second_elements.append(element)
    return second_elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

#Combination of name and email as one string in a list:
def full_emails(people):
    full_result = []
    for email, name in people:
        full_result.append("{} {}".format(name.email))
    return full_result

#print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))

# Creating list quick & easy way based on sequences or ranges -> List Comprehension
# Normal list
multiples = []
for x in range (1, 11):
    multiples.append(x*7)
print(multiples) # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# List Comprehension
multiples = [x*7 for x in range(1,11)]
print(multiples)  #[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

languages = ("Python", "Perl", "Ruby", "Go", "Java", "C")
lengths = [len(language)for language in languages]
print(lengths)          #[6, 4, 4, 2, 4, 1]

z = [x for x in range(0,101) if x % 3 == 0]
print(z)
#[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

#The odd_numbers function returns a list of odd numbers between 1 and n, inclusively.
# Fill in the blanks in the function, using list comprehension.
# Hint: remember that list and range counters start at 0 and end at the limit minus 1.

def odd_numbers(n):
	return [x for x in range (1, n) if x % 2 == 1]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

#List Comprehensions
# You can create lists from sequences using a for loop, but there’s a more streamlined way to do this: list
# comprehension. List comprehensions allow you to create a new list from a sequence or a range in a single line.

#For example, [ x*2 for x in range(1,11) ] is a simple list comprehension. This would iterate over the range 1 to 10,
# and multiply each element in the range by 2. This would result in a list of the multiples of 2, from 2 to 20.

#You can also use conditionals with list comprehensions to build even more complex and powerful statements.
# You can do this by appending an if statement to the end of the comprehension. For example, [ x for x in range(1,101)
# if x % 10 == 0 ] would generate a list containing all the integers divisible by 10 from 1 to 100. The if statement
# we added here evaluates each value in the range from 1 to 100 to check if it’s evenly divisible by 10. If it is,
# it gets added to the list.

#List comprehensions can be really powerful, but they can also be super complex, resulting in code that’s hard to read.
# Be careful when using them, since it might make it more difficult for someone else looking at your code to easily
# understand what the code is doing.

#Question 1
# Given a list of filenames, we want to rename all the files with extension hpp to the extension h.
# To do this, we would like to generate a new list called newfilenames, consisting of the new filenames.
# Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or
# a list comprehension.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
newfilenames = []
# using as many lines of code as your chosen method requires.
for file in filenames:
    newfilenames.append(file)

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


