# Create a function that takes a string as an argument and returns a list
# with all leading sub-strings of that string that are shorter than 5 letters,
# starting from the longest to the shortest. For example:

def all_lead_substr(string):
    stop = len(string) if len(string) <= 4 else 4
    result = []

    while stop >= 1:
        result.append(string[0:stop])
        stop -= 1
    
    return result

# PSEUDOCODE:
# stop = 4
# LOOP: while stop >= 1:
# substring = string[0:stop] 'abcd'
# stop -= 1 => 3
# substring = string[0:stop] 'abc'
# ..
# stop => 1
# substring = string[0:stop] 'a'

# append substring to a list on each iteration of loop.

# list.sort(key=len, reverse=True)
print(all_lead_substr('abcdefg')) #; //=> ['abcd', 'abc', 'ab', 'a'];
print(all_lead_substr('abcde')) #; //=> ['abcd', 'abc', 'ab', 'a'];
print(all_lead_substr('abcd')) #; //=> ['abcd', 'abc', 'ab', 'a'];
print(all_lead_substr('ab')) #; //=> ['ab', 'a'];