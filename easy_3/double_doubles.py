# Write a function that returns the number provided as an argument multiplied
# by two, unless the argument is a double number. If the argument is a double
# number, return the double number as-is.

# PSEUDOCODE:
# Get the number, convert to a string.
# IF it has an even number of digits (length):
#     IF SUBPROCESS its first half matches the second half:
#       return it as is
# ELSE:
#   return the number * 2

# SUBPROCESS first half matching second half:
# GET the half length of the string number (len(string) / 2)
# Compare the first half of the string with the second half using index slicing
# and using that half length number

def twice(num):
    double_num = num * 2
    num_string = str(num)
    half_index = len(num_string) // 2

    if len(num_string) % 2 == 0 and\
        num_string[:half_index] == num_string[half_index:]:
        return num
    else:
        return double_num
    
def twice(num):
    double_num = num * 2
    num_string = str(num)
    half_index = len(num_string) // 2

    if num_string[:half_index] == num_string[half_index:]:
        return num
    else:
        return double_num
    
def twice(num):
    double_num = num * 2
    num_string = str(num)
    half_index = len(num_string) // 2

    return double_num if num_string[:half_index] != num_string[half_index:]\
    else num


print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True