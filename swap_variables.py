# swap a value with b value without using a third variable

def swap_vars(a, b):
    print(f"A = {a} and B = {b}")
    a = a + b
    b = a - b
    a = a - b
    print(f"A = {a} and B = {b}")


a = int(input("Input value of a: "))
b = int(input("Input value of b: "))

swap_vars(a, b)

