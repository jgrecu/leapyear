def count_substring(string, sub_string):
    counts = 0
    for i in range(0, len(string)):
        temp_s = string[i:i+len(sub_string)]
        if temp_s == sub_string:
            counts += 1
    return counts


string = input("Input string: ").strip().lower()
sub_string = input("Input Substring: ").strip().lower()

count = count_substring(string, sub_string)
print(count)
