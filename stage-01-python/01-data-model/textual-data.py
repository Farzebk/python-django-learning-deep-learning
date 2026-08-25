print("Hello, World!")

message = "Welcome to the Python programming language."

print(message)

use_single_ticks = 'This is a string using single quotes.'

use_double_ticks = "This is a string using double quotes."

use_triple_single_ticks_for_multiline = '''This is a string
that spans multiple lines'''

use_triple_double_ticks_for_multiline = """This is another string
that spans multiple lines"""

print(use_triple_double_ticks_for_multiline, "line22")

use_escape_characters = "This is a string with an escape character: \"Hello!\""

use_apostrophes_in_strings = "It's a beautiful day!"

print(len(message))  # Prints the length of the message string

print(message[0])  # Prints the first character of the message string

print(message[-1])  # Prints the last character of the message string

# print(message[222]) # error: IndexError: string index out of range

print(message.lower())  # Converts the message string to lowercase

print(message.capitalize())  # Capitalizes the first character of the message string

print(message.upper())  # Converts the message string to uppercase

print(message.count("o"))  # Counts the occurrences of the letter "o" in the message string

print(message.find("Python"))  # Finds the index of the substring "Python" in the message string

print(message.replace("Python", "Java"))  # Replaces "Python" with "Java" in the message string

greeting = "Hello"
name = "Alice"

print(greeting + ", " + name + "!")  # Prints "Hello, Alice!"

print(f"{greeting}, {name}!")  # Prints "Hello, Alice!" using f-string formatting

print(dir(message))  # Prints a list of all the attributes and methods of the message string

print(help(str))  # Prints the help documentation for the str class


