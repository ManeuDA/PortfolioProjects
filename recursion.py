# Recursion
# The repeated appilcation of the same procedure to a smaller problem
# Maxium Recusion depth is less than 1000

#a recursive function will usually have this structure:
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)


def factorial(n):
    print("Factorial called with " +str(n))
    if n < 2:       #base case
        print("Returning 1")
        return 1
    result = n * factorial(n-1)  # Recursive case - function is calling itself with (n-1) smaller number
    print("Returning " + str(result) + " for factorial of " +str(n))
    return result

print(factorial(4))
#Factorial called with 4
#Factorial called with 3
#Factorial called with 2
#Factorial called with 1
#Returning 1
#Returning 2 for factorial of 2
#Returning 6 for factorial of 3
#Returning 24 for factorial of 4

# Question: The function sum_positive_numbers should return the sum of all positive numbers between the number n
# received and 1. For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.
# Fill in the gaps to make this work:

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

#Question: Fill in the blanks to make the is_power_of function return whether the number is a power of the given base.
# Note: base is assumed to be a positive number. Tip: for functions that return a boolean value, you can
# return the result of a comparison.

def is_power_of(number, base):
  # Base case: when number is smaller than base.
    if number == 1:
        return True
    elif base == 0 or number % base !=0 or number < base:
        return False
    return is_power_of(number//base, base)
  # Recursive case: keep dividing number by base.

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

#The count_users function recursively counts the amount of users that belong to a group in the company system,
# by going through each of the members of a group and if one of them is a group, recursively calling the function
# and counting the members. But it has a bug! Can you spot the problem and fix it?


def count_users(group):
  count = 0
  for member in get_members(group):
    count += 1
    if is_group(member):
      count += count_users(member)-1

  return count


#Implement the sum_positive_numbers function, as a recursive function that returns the sum of all positive numbers
# between the number n received and 1. For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should
# return 1+2+3+4+5=15.

def sum_positive_numbers(n):
  if n <=1:
      return n
  result = n + sum_positive_numbers(n-1)
  return result

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

#Question 3 Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2
# digits and 144 has 3 digits. Tip: you can figure out the digits of a number by dividing it by 10 once per digit
# until there are no digits left.

def digits(n):
    count = 0
    if n == 0:
        return 1
    while n > 0:
        count += 1
        n = n // 10
    return count


print(digits(25))  # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))  # Should print 1