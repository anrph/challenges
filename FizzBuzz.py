# Challenge #1

# THE FAMOUS "FIZZ BUZZ"
# Difficulty: EASY
# Statement: Write a program that displays through the console (with a print) the numbers from 1 to 100 (both included and with a line break between each print), substituting the following:
# - Multiples of 3 for the word "fizz".
# - Multiples of 5 for the word "buzz".
# - Multiples of 3 and 5 at the same time for the word "fizz buzz".

def try1():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

def try2():
    for index in range(1, 101):
        output = ""
        if index % 3 == 0:
            output += "fizz"
        if index % 5 == 0:
            output += "buzz"
        print(output if output else index)

if __name__ == "__main__":
    try2()
