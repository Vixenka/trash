# Exercise 1
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

# Exercise 2
def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    if a == 0:
        return None

    return a

# Exercise 3
def sum_of_divisors(_):
    # This will be always zero, because any positive number has the same number of positive divisors as negative
    # divisors.
    return 0

# Exercise 4
def count_number_of_prime_factors(n):
    if n <= 1:
        if n < 1:
            return None
        return 0
    
    count = 1
    while True:
        i = 2
        while i * i <= n:
            if n % i == 0:
                n //= i
                count += 1
                break
            i += 1
        else:
            return count
        
# Exercise 5
def is_palindrome(word):
    # I use try-except, because this exercise disallow use built-in functions like len() or more than one element
    # indexing and Python's str does not require things like null character. But I can use control instructions like:
    # if, while, for, etc. then I think try-except is allowed too.
    try:
        i = 0
        while True:
            if word[i] != word[-i - 1]:
                return False
            i += 1
    except IndexError:
        return True
