# Create a function that takes a string as an argument and returns an array
# with all leading sub-strings of that string. For example:

def all_lead_substr(string):
    result = []
    stop = 1

    while stop <= len(string):
        result.append(string[0:stop])
        stop += 1

    return result
print(all_lead_substr('abcd')) #; // => ['a', 'ab', 'abc', 'abcd'];