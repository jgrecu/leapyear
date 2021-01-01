# take input an integer, i.e. 5 and print the ordered string like 12345, or 3 print 123, or 7 print 1234567
n = int(input(":"))
ranges = ""
for i in range(1, n+1):
    ranges += str(i)
print(ranges)
