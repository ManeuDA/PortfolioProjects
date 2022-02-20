# Use while loops when you want to repeat an action util a condition changes
# Use for loops when there's a sequence of elements that you want to iterate

#Things to watch out for!
# 1. Failure to initialize variables. Make sure all the variables used in the loop’s condition
# are initialized before the loop.
# 2. Unintended infinite loops. Make sure that the body of the loop modifies the variables used in the condition,
# so that the loop will eventually end for all possible values of the variables.

# While Loop
x = 0       #initializing
while x < 5:
    print ("Not there yet, x =" + str(x))   # while loop body
    x = x + 1                               # while loop body
print("x = " + str(x))
#Answer: Not there yet, x =0, Not there yet, x =1, Not there yet, x =2, Not there yet, x =3, Not there yet, x =4, x = 5

# Anatomy of a While Loop
# A while loop will continuously execute code depending on the value of a condition.
# It begins with the keyword while, followed by a comparison to be evaluated, then a colon. On the next line is
# the code block to be executed, indented to the right. Similar to an if statement, the code in the body will only
# be executed if the comparison is evaluated to be true. What sets a while loop apart, however, is that this
# code block will keep executing as long as the evaluation statement is true. Once the statement is no longer true,
# the loop exits and the next line of code will be executed.

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1          # equals expression x = x + 1
    print("Done")

attempts(5)
#Answer: Attempt 1, Attempt 2, Attempt 3, Attempt 4, Attempt 5, Done

# Why Initializing variables matters
def count_down(start_number):
  current = 3                       # Initialization
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3) #Answer: 3, 2, 1, Zero

# Common Pitfalls With Variable Initialization
# You'll want to watch out for a common mistake: forgetting to initialize variables. If you try to use a variable
# without first initializing it, you'll run into a NameError. This is the Python interpreter catching the mistake
# and telling you that you’re using an undefined variable. The fix is pretty simple: initialize the variable
# by assigning the variable a value before you use it.

# Another common mistake to watch out for that can be a little trickier to spot is forgetting to initialize variables
# with the correct value. If you use a variable earlier in your code and then reuse it later in a loop without first
# setting the value to something you want, your code may wind up doing something you didn't expect. Don't forget to
# initialize your variables before using them!

# If x != 0:      # If x is not 0
    # while x % 2 == 0    # while remainder is 0
        # x = x / 2       # divide x / 2

# or

# while x != 0 and x % 2 == 0:
   # x = x /2

def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n += 1

print_range(1, 5)  # Should print 1 2 3 4 5


def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    while n != 0 and n % 2 == 0:
        n = n / 2
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    return False


print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False

#Fill in the empty function so that it returns the sum of all the divisors of a number, without including it.
# A divisor is a number that divides into another without a remainder.

def sum_divisors(n):
    sum = 0
    x = 1
    while n != 0 and x < n:
        if n % x == 0:
            sum += x
        else:
            sum += 0
        x += 1

    return sum


print(sum_divisors(0))
# 0
print(sum_divisors(3))  # Should sum of 1
# 1
print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51
# 114


#The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5.
# An additional requirement is that the result is not to exceed 25, which is done with the break statement.
# Fill in the blanks to complete the function to satisfy these conditions.

def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number * multiplier
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24


# Fill in the blanks of this code to print out the numbers 1 through 7.
number = 1
while number < 7:
	number = number + 1
	print(number)

# Question 5
# The counter function counts down from start to stop when start is bigger than stop, and counts up from start to
# stop otherwise. Fill in the blanks to make this work correctly.

def counter(start, stop):
    x = start
    if x > stop:
        return_string = "Counting down: "
        while x > stop:
            return_string = return_string + str(x) + ","
            x -= 1
            if x == stop:
                return_string = return_string + str(x)
    elif x < stop:
        return_string = "Counting up: "
        while x < stop:
            return_string = return_string + str(x) + ","
            x += 1
            if x == stop:
                return_string = return_string + str(x)
    else:
        return_string = "Counting up: "
        if x == stop:
            return_string = return_string + str(x)

    return return_string

print(counter(1,10))  # Counting up: 1,2,3,4,5,6,7,8,9,10
print(counter(2,1))    # Counting down: 2, 1
print(counter(5,5))     # Counting up: 5