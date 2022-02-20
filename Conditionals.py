  
def hint_username(username):
    if len(username) < 3:
        print("Invalid username, Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")

def is_positive(number):
  if number > 0 :
    return True
  else:
    return False

number=is_positive(0)
print(number)            #Answer: False

def is_even(number):
    if number % 2 == 0:              # % remainder integer after division
        return True
    return False                    # In this case, else block is not needed because if statement is false, it will
                                    # not excuted, and only return Flase will be excuted

def number_group(number):
  if number > 0:
    return "Positive"
  elif number == 0:
    return "Zero"
  else:
    return "Negative"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative

def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))       #Answer: Welcome back Taylor!
print(greeting("John"))      #Answer: Hello there, John
print((2*2) == 4)             #Answer: True


def calculate_storage(filesize):
    block_size = 4096
    if filesize == 1:
        filesize = block_size
        return filesize
        # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize % block_size == 0
        # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size > 0
        # Depending on whether there's a remainder or not, return
        # the total number of bytes required to allocate enough blocks
        # to store your data.
    if partial_block_remainder > 0:
        return 4096 * 2
    return 4096


print(calculate_storage(1))  # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192



def format_name(first_name, last_name):
	if len(first_name) > 1 and len(last_name) > 1:
		print("Name:" + last_name, first_name)
	elif len(first_name) >1 and len(last_name) == 0:
		print("Name:" + first_name)
	elif len(first_name) == 0 and len(last_name) > 1:
		print("Name:" + last_name)
	else:
		print("")

print(format_name("Ernest", "Hemingway"))  #Answer Name:Hemingway Ernest
print(format_name("Voltaire", ""))      #Answer Name:Voltaire
print(format_name("", ""))              #Answer None

print(type(0.2))            #<class 'float'>

def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to
# keep just the fractional part of the quotient
	if denominator == 0 or numerator == 0:
		return 0
	elif numerator % denominator == 0:
		return 0


print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

print("big" > "small")
print(11%5)         #Answer: 1


def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))  #Answer:10

print((10 >= 5*2) and (10 <= 5*2))  #Answer: True
