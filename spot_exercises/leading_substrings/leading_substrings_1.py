# Create a function that takes a string as an argument and returns an list
# with all leading sub-strings of that string that are 3 letters or longer.
# For example:

def all_lead_substr(string):
    stop = 3
    result = []

    if len(string) >= stop:
        while stop <= len(string):
            result.append(string[0:stop])
            stop += 1
        return result
    else:
        return string

def all_lead_substr(string):
    result = []

    if len(string) > 2:
        return [string[:idx] for idx in range(3, len(string) + 1)]
    else:
        return string

# PSEUDOCODE:
# index = 3
# substring = string[0:index] - 'abc'
# substring = string[0:index] - 'abcd'
# substring = string[0:index] - 'abcde'
# ...
# substring = string[0:len(string)] - 'abcdef'

# append substring to a list on each iteration of the loop
# return the list

print(all_lead_substr('abcdef')) # //=> ['abc', 'abcd', 'abce', 'abcdef']
print(all_lead_substr('abcdefghij'))
print(all_lead_substr('ab')) # => 'ab'
print(all_lead_substr('abc')) # => ['abc']