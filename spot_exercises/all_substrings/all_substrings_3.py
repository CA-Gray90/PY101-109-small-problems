# Create a function that takes a string as an argument and returns an array
# with all the sub-string of given string that are exactly 3 letters long.

def all_substr(string):
    result = []

    for idx in range(0, len(string)):
        substring = string[idx:idx + 3]

        if len(substring) == 3:
            result.append(substring)
        
    return result

def all_substr(string):

    return [string[idx:idx + 3] for idx in range(0, len(string))\
            if len(string[idx:idx +3]) == 3]


print(all_substr('abcd')) #; // => ['abc', 'bcd'];
print(all_substr('abcdef')) #; // => ['abc', 'bcd', 'cde', 'def'];