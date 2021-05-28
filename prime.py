def is_prime(num):
    """ Return True is the number is prime. """
    if num < 2:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

def primes_lessthan(number):
    """ Return a list of all prime numbers less than n. """
    result = []
    for i in range(2, number):
        if is_prime(i):
            result.append(i)
    return result

print(primes_lessthan(50))
