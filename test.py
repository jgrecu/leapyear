def sum_divisors(n):
    sum = 0
    # Return the sum of all divisors of n, not including n
    x = 1
    if n == 0:
        return sum
    else:
        while n != x:
            if n % x == 0:
                sum += x
            x += 1
    return sum


print(sum_divisors(36))
print(sum_divisors(102))
