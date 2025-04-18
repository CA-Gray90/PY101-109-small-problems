# Create a function that takes a string as an argument and returns an array
# with all the sub-string of given string that are longer than 1 letter.

def all_substr(string):
    result = []

    for idx in range(0, len(string)):
        substring = string[idx:]
        stop = 2 # get substrings of length 2 or more

        while stop <= len(substring):
            result.append(substring[:stop])
            stop += 1
        
    return result

# For example:
print(all_substr('abcd'))#;//=> ['ab', 'abc', 'abcd', 'bc', 'bcd', 'cd'];