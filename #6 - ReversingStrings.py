# Challenge #6

# REVERSING STRINGS
# Create a program that reverses the order of a text string without using language functions that do it automatically.
# - If we passed "Hello world" it would return "dlrow olleH"


# String reverser function
def reverse_string(input_string):
    reversed_string = ""
    # Iterate over every single letter from the input string starting from the right.
    for i in range(len(input_string) - 1, -1, -1):
        # Add the letter to the reversed string
        reversed_string += input_string[i]
    return reversed_string

# Example string
input_string = "Hello world"
# Print reversed string
print(reverse_string(input_string))