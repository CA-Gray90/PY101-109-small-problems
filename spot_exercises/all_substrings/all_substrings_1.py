# Create a function that takes a string as an argument and returns an array
# with all the sub-strings of the given string.

def all_sub_str(string):
    result = []

    for idx in range(0, len(string)):
        substring = string[idx:]
        stop = 1

        while stop <= len(substring):
            result.append(substring[0:stop])
            stop += 1
    
    return result
        
# PSEUDOCODE:
# result = []
#
# LOOP: for idx, char in enumerate(string) => 'a', 'b', 'c', 'd'
# idx = 0
# substring = string[idx:]
# stop = 1
# while stop <= len(substring)
# substring = string[0:stop]
# append substring to result
# stop += 1
# substring = string[0:stop]'ab'
# substring = 'abc'
# substring = 'abcd'
# ...

print(all_sub_str('abcd')) # ; //=> ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']
print(all_sub_str('ab'))
print(all_sub_str('abcdef'))