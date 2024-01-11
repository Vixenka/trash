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
def sum_of_positive_divisors(n):
    if n < 1:
        return None

    sum = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            sum += i
            if i * i != n:
                sum += n // i
        i += 1
    
    return sum

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
    len = 0
    for _ in word:
        len += 1
    
    for i in range(len // 2):
        if word[i] != word[-1 - i]:
            return False
        
    return True
