def is_prime(n):
    """
    Efficient primality test using 6k±1 optimization.
    """
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

# Sum primes between 3 and 1000
prime_sum = sum(i for i in range(3, 1001) if is_prime(i))
print("Sum of primes between 3 and 1000:", prime_sum)
