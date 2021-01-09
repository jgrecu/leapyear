
def get_factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * get_factorial(n-1)


print(get_factorial(4))
