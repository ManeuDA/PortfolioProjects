# Functions

def greeting(name, department):
    #use def, variable name and passing values as parameters in () separated by coma
    print("Welcome, " + name)
    print("You are part of " + department)
greeting("Anja", "IT Support.")     # Answer:   Welcome, Anja # You are part of IT Support.
greeting ("Sophie", "Human Resources.")     #Answer: Welcome, Sophie # You are part of Human Resources.

# Return values - getting values out of function
# example 1
def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is:" + str(sum))       # Answer: The sum of both areas is:20.5

#example 2 We can return value to use it to get more than one value
def converts_seconds(seconds):
    hours = seconds//3600    # // (floor division) divide and give integer numbers and not float
    minutes = (seconds - hours*3600)//60
    remaining_seconds = seconds - hours*3600 - minutes*60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = converts_seconds(5000)
print(hours, minutes, seconds)          # 1 23 20

# None because there was no return statement in the function
# None is a special data type in Python used to indicate that things are empty or that they returned nothing
def greeting(name):
    print("Welcome, " + name)
result = greeting("Christine")
print(result)                   #Answer: Welcome, Christine

# Returning Values Using Functions
# Sometimes we don't want a function to simply run and finish. We may want a function to manipulate data we passed it
# and then return the result to us. This is where the concept of return values comes in handy. We use the return
# keyword in a function, which tells the function to pass data back. When we call the function, we can store
# the returned value in a variable. Return values allow our functions to be more flexible and powerful,
# so they can be reused and called multiple times.

# Functions can even return multiple values. Just don't forget to store all returned values in variables!
# You could also have a function return nothing, in which case the function simply exits.

# Principle of Code Reuse - when the same code is use multiple time, use a function to clean up the codes
name = input("Enter your name here: ")
def lucky_number(name):
    number = len(name) * 9
    print ("Hello " + name + ". Your lucky number is " + str(number))

lucky_number(name) #Answer: Enter your name here: Andre # Hello Andre. Your lucky number is 45

#Code Style
# Self-documenting code - written in a way that's readable and doesn't conceal its intent
# refactor - renaming the variable so that it is easy to understand

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = 55


# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))
# Answer: The distance in kilometers is 88.0


# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
round_trip = float (my_trip_km) * 2
print("The round-trip in kilometers is " + str(round_trip))
# Answer: The round-trip in kilometers is 176.0

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)
#Answer: 99 100

#Flesh out the body of the print_seconds function so that it prints the total amount of seconds given the hours,
# minutes, and seconds function parameters. Remember that there are 3600 seconds in an hour and 60 seconds in a minute.

def print_seconds(hours, minutes, seconds):
    hours = hours * 3600
    minutes = minutes * 60
    seconds = seconds *1
    total_seconds = hours + minutes + seconds
    return total_seconds
    print(total_seconds)

print(print_seconds(1,2,3))  # Answer: 3723