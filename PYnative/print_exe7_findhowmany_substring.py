x = '''
Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.

Given:

str_x = "Emma is good developer. Emma is a writer"
Expected Output:

Emma appeared 2 times
'''

str_x = "Emma is good developer. Emma is a writer"
number_of_count = str_x.count("Emma")

print(f"Emma appeared {number_of_count} times")