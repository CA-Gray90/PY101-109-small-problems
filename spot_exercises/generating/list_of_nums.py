# Create a function that takes two arguments: starting number and end number
# and returns a list with numbers starting from start_num and ending on
# end_num.

def generate_list(start, end):

    if start > end:
        step = -1
        end -= 1
    else:
        step = 1
        end += 1

    result = list(range(start, end, step))
    return result

# PSEUDOCODE:
# create an empty list - result
# LOOP; while start != end:
# append start num to list
# add 1 to start
# exit loop
# append end num to list
# return list

# For example:
print(generate_list(3, 10)) # [3, 4, 5, 6, 7, 8, 9, 10]
print(generate_list(3, 3)) #
print(generate_list(10, 3)) # [10, 9, 8 .. 3]