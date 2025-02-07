# Write a function that takes a non-empty string argument and returns the
# middle character(s) of the string. If the string has an odd length, you
# should return exactly one character. If the string has an even length, you
# should return exactly two characters.

def center_of(string):
    if string:
        if len(string) % 2 == 0:
            middle_index = (len(string) // 2) - 1
            return string[middle_index:middle_index + 2]
        else:
            return string[len(string) // 2]
        
def center_of(string):
    if string:
        length = len(string)
        middle_index = length // 2
        if length % 2 == 0:
            return string[middle_index - 1:middle_index + 1]
        else:
            return string[middle_index]
    return string
        
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True
print(center_of('xo') == "xo")                  # True
print(center_of('') == '')                      # True