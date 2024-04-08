# Challenge #2

# The Fibonacci sequence
# Write a program that prints the first 50 numbers of the Fibonacci sequence starting at 0.
# - The Fibonacci series is made up of a sequence of numbers in which the next one is always the sum of the previous two.
#   0, 1, 1, 2, 3, 5, 8, 13...

def main():
    fibo = [0, 1]
    for i in range(2, 50):
        next_fibo = fibo[i - 1] + fibo[i - 2]
        fibo.append(next_fibo)

    print(fibo)

if __name__ == "__main__":
    main()