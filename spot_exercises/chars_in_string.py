# Create a function that takes a string as an argument and return an object
# with letters of the string and their occurrence as properties:

def count_occurencies(string):
    result = {}

    for char in string:
        if char in result.keys():
            continue
        result[char] = string.count(char)
    
    return result

# PCODE
# result = {}
# LOOP through chars in string:
# if char in dict as key already: skip this iteration of the loop
# for each char, create a key of that char add the count as value
# loop exits
# return result

print(count_occurencies('abbab')) # ; => {a:2, b: 3} # a b
print(count_occurencies('abbbcbzcabc')) # a b c z

# Create a function that takes the object that your function returned as an
# argument and returns a string with all the letters that appears in the
# object, in alphabetical order appearing as many times as the value states.
# Order doesn't matter.

def produce_string(dictionary):
    result_list = []

    for key, value in dictionary.items():
        result_list.append(key * value)

    result_list.sort()
    result_string = ''.join(result_list)

    return result_string

# PCODE
# SET empty string to `result`
# LOOP through dict:
# set a var to current key of dict and another var to current value of key
# result += current key of dict * value of current key
# loop exits
# return result string

print(produce_string(count_occurencies('abbbcbzcabc'))) # 'aabbbbbcccz'
print(produce_string(count_occurencies('abbab'))) # 'aabbb'
print(produce_string(count_occurencies('azzcbab'))) # 'aabbczz'