def is_prime(n):
    """Check if a number is prime"""
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
two_digit_primes=[n for n in range(10,100)if is_prime(n)]
print("Two-digit prime numbers:", two_digit_primes)