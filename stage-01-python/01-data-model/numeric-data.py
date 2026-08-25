num = 9

print(type(num))  # Prints the type of the variable num - class 'int'

num1 = 3

print(type(num1))  # Prints the type of the variable num1 - class 'float'

# arithmetic operations
sum_result = num + num1  # Addition
subtraction_result = num - num1  # Subtraction
multiplication_result = num * num1  # Multiplication
division_result = num / num1  # Division

floor_division_result = num // num1  # Floor Division
exponentiation_result = num ** num1  # Exponentiation
modulus_result = num % num1  # Modulus

print( 3 * 1 + 2)  # Prints the result of 3 multiplied by 1 plus 2 which is 5
print( 3 * (1 + 2))  # Prints the result of 3 multiplied by the sum of 1 and 2 which is 9

number = 10
number = number + 5 # Adds 5 to the current value of number
number += 5 # Shorthand for adding 5 to the current value of number

print(abs(-5))  # Prints the absolute value of -5 which is 5

print(round(3.76))  # Prints the rounded value of 3.76 which is 4
print(round(3.76, 1))  # Prints the rounded value of 3.76 to 1 decimal place which is 3.8

#comparison operators
equal = (num == num1)  # Checks if num is equal to num1
not_equal = (num != num1)  # Checks if num is not equal to num1
greater_than = (num > num1)  # Checks if num is greater than num1
less_than = (num < num1)  # Checks if num is less than num1
greater_than_or_equal = (num >= num1)  # Checks if num is greater than or equal to num1
less_than_or_equal = (num <= num1)  # Checks if num is less than

print(num1 < num)  # Prints the remainder of num divided by num1 which is 0

num_1 = "100"

num_2 = "200"

print(num_1 + num_2)  # Concatenates the two strings num_1 and num_2, resulting in "100200"

print(int(num_1) + int(num_2))  # Converts the strings num_1 and num_2 to integers and adds them, resulting in 300
