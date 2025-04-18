# Create a function that takes a string as an argument and returns a boolean
# value, true if the word is a pangram and false if it's not. A pangram contains
# all letters from the alphabet.

def is_pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in alphabet:
        if char not in string.lower():
            return False
    
    return True

# PSEUDOCODE:
# LOOP through the letters of the alphabet:
# For each char, check that that character is not in `string`:
# Return False
# If we finish the loop, return True

print(is_pangram("The quick brown fox jumped over the lazy sleeping dog,")) # //true
print(is_pangram('abcd')) # //false
print(is_pangram('Bawds jog, flick quartz, vex nymphs')) # //true