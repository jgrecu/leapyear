# swap a value with b value without using a third variable

a = int(input("Input value of a: "))
b = int(input("Input value of b: "))

print(f"A = {a} and B = {b}")
# logical way
# a = a + b
# b = a - b
# a = a - b
# print(f"A = {a} and B = {b}")

# python function way
def swap(a, b):
    return b, a


a, b = swap(a, b)
print(f"A = {a} and B = {b}")
