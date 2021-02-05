def is_prime(num):
    """ Return True is the number is prime. """
    prime = True
    for n in range(2, num):
        if num % n == 0:
            # print(f"{num} % {n} = {num%n}")
            prime = False
    return prime

def primes_lessthan(n):
    """ Return a list of all prime numbers less than n. """
    result = []
    for i in range(2,n):
        if is_prime(i):
            result.append(i)
    return result

print(primes_lessthan(500))
