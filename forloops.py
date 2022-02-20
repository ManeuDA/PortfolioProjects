#for loop - iterates over a sequence of values
# Use while loops when you want to repeat an action util a condition changes
# Use for loops when there's a sequence of elements that you want to iterate

#Common pitfalls:
# 1. Forgetting that the upper limit of a range() isn’t included.
# 2. Iterating over non-sequences. Integer numbers aren’t iterable. Strings are iterable letter by letter,
# but that might not be what you want.

#Typical use:
# For loops are mostly used when there's a pre-defined sequence or range of numbers to iterate.

# Break & Continue
# You can interrupt both while and for loops using the break keyword.
# We normally do this to interrupt a cycle due to a separate condition.
# You can use the continue keyword to skip the current iteration and continue with the next one.
# This is typically used to jump ahead when some of the elements of the sequence aren’t relevant.
# If you want to learn more, check out this wiki page on for loops.


for x in range(5):
    print(x)                # Answer: 0, 1, 2, 3, 4

# Range
    #1 In Python (and a lot of other programming languages=, a range of numbers will start with 0 by default
    #2 The list of numbers generated will be one less than the given value

#the sum_squares function, it returns the sum of all the squares of numbers between 0 and x (not included).
def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)            #equals sum = sum + square(n)
    return sum

print(sum_squares(10)) # Should be 285

# for fuctions can be used for any text and number values
values = [23, 52, 59, 37, 48]
#intitlizing variables for for loop
sum = 0
length = 0
for value in values:        #for loop and for loop body (below content)
    sum += value    # equals sum = sum + value
    length += 1     # equals length = lenght + 1
print("Total sum: " + str(sum) + " - Average: " + str(sum/length))
# Answer: Total sum: 219 - Average: 43.8

#Question
#In math, the factorial of a number is defined as the product of an integer and all the integers below it.
# For example, the factorial of four (4!) is equal to 1*2*3*4=24. Fill in the blanks to make the factorial
# function return the right number. Pay attention at the operations that the code is
# doing and make sure that the factorial function returns the
# product of the numbers between 1 and n.
def factorial(n):
    result = 1
    for n in range (1, n+1):
        result = result * n
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

# for loop in 3 ranges (starting point, end point, numbers skipped between execution)
# Don't forget that second range won#t contain the last element; it will stop one bofore the parameter specified.
# Three parameters will create a sequence starting with the first parameter and stopping before the second parameter,
# but this time increasing each step by the third parameter
def to_celsius(x):
    return (x-32)*5/9
for x in range (0,101,10):
    print(x, to_celsius(x))
 # 0 -17.77777777777778
 #10 -12.222222222222221
 #20 -6.666666666666667
 #30 -1.1111111111111112
 #40 4.444444444444445
 #50 10.0
 #60 15.555555555555555
 #70 21.11111111111111
 #80 26.666666666666668
 #90 32.22222222222222
 #100 37.77777777777778


#Nested for Loops --> Only use for short tasks, otherwise it will take much longer to finish tasks
for left in range(7):
    for right in range (left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end = " ")      #new parameter "end" creates new line
    print()
#[0|0] [0|1] [0|2] [0|3] [0|4] [0|5] [0|6]
#[1|1] [1|2] [1|3] [1|4] [1|5] [1|6]
#[2|2] [2|3] [2|4] [2|5] [2|6]
#[3|3] [3|4] [3|5] [3|6]
#[4|4] [4|5] [4|6]
#[5|5] [5|6]
#[6|6]

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)
#Dragons vs Wolves
#Dragons vs Pandas
#Dragons vs Unicorns
#Wolves vs Dragons
#Wolves vs Pandas
#Wolves vs Unicorns
#Pandas vs Dragons
#Pandas vs Wolves
#Pandas vs Unicorns
#Unicorns vs Dragons
#Unicorns vs Wolves
#Unicorns vs Pandas

# print from 0 -24 --> Use range
for x in range (25):
    print(x)


# If you want to call only number 25 in the list, then use
for x in [25]:
    print(x)#Answer: 0, 1,2, 3,4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends(['Taylor', 'Lucia', 'Jamal', 'Eli']) #Hi Taylor, Hi Lucia, Hi Jamal
greet_friends("Barry")      #Hi B, Hi a, Hi r, Hi r, Hi y
greet_friends(["Barry"])        #Hi Barry
#But if you forget the [] outside name, then string will iterate. Make sure the name is in the []

#The validate_users function is used by the system to check if a list of users is valid or invalid.
# A valid user is one that is at least 3 characters long. For example, ['taylor', 'luisa', 'jamaal'] are all
# valid users. When calling it like in this example, something is not right. Can you figure out what to fix?

def validate_users(users):
  for user in users:
    if len(user) > 3:
      print(user + " is valid")
    else:
      print(user + " is invalid")

validate_users(["purplecat"])           #Answer: purplecat is valid

#Question 2 Fill in the blanks to make the factorial function return the factorial of n. Then, print the first
# 10 factorials (from 0 to 9) with the corresponding number. Remember that the factorial of a number is defined
# as the product of an integer and all integers before it. For example, the factorial of five (5!) is
# equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.

def factorial(n):
    result = 1
    for n in range(1,n):
        result = result * n
    return result

for n in range(0 ,10):
    print(n, factorial(n+1))
#0 1, 1 1, 2 2, 3 6, 4 24, 5 120, 6 720, 7 5040, 8 40320, 9 362880

# Question 3 Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.

for x in range(1,11):
  x = x**3
  print(x)      #1, 8, 27, 64, 125, 216, 343, 512, 729, 1000

# Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing
# any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.
def multiple_7(n):
    n = 7 * n
    return n
for n in range (0,15):
    print (multiple_7(n)) # 0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98

# Question 5 The retry function tries to execute an operation that might fail, it retries the operation for a number
# of attempts.  Currently the code will keep executing the function even if it succeeds. Fill in the blank so the
# code stops trying after the operation succeeded.

def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")


#This function prints out a multiplication table (where each number is the result of multiplying the first number of
# its row by the number at the top of its column). Fill in the blanks so that calling multiplication_table(1, 3)
# will print out:
#1 2 3
#2 4 6
#3 6 9

def multiplication_table(start, stop):
	for x in range(start, stop+1):
		for y in range(start, stop+1):
			print(str(x*y), end = " ")
		print()
print(multiplication_table(1, 3))

# Should print out the multiplication table above

for x in range(1, 10, 3):
    print(x)
# 1, 4, 7
for x in range(10):
    for y in range(x):
        print(y)

#Answer 0 01 012 0123 0124 0125 0126 0127 0128