# Challenge #4

# IS IT A PRIME NUMBER?
# Write a program that is responsible for checking whether a number is prime or not.
# Then print the prime numbers between 1 and 100.

# Range of numbers to check
nums = range(1,101)


def is_prime(num):
    # Numbers less than or equal to 1 are not prime
    if num <= 1:
        return False

    # Check for factors from 2 to num -1
    for i in range(2,num):
        # If num is divisible by i, it is not a prime number
        if (num % i) == 0:
            return False
        
    # If no divisors are found, num is prime
    return True


# Filter to apply the is_prime function to each number in nums and then list the results.
primes = list(filter(is_prime, nums))

# Print the prime numbers list
print(primes)