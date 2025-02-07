# Write a function that returns the next to last word in the string argument.

def penultimate(string):
    return string.split()[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

# Write a function that returns the middle word of a phrase or sentence.
# It should handle all of the edge cases you thought of.

def middle_word(sentence):
    words_list = sentence.split()
    list_length = len(words_list)

    if list_length > 2 and list_length % 2 != 0:
        middle_word = words_list[(list_length // 2)]
        return middle_word.strip(',.?!:;"\'')
    
    return None 

print(middle_word(''))                          # None
print(middle_word('Hello there'))               # None
print(middle_word('Hello there! charlie'))      # 'there'
print(middle_word('Hello there, charlie'))      # 'there'
print(middle_word('Hello there charlie brown')) # None
print(middle_word('Hello there charlie brown, the quick brown fox jumped over the lazy dog'))
print(middle_word('Hello there charlie! what\'s up?'))



# edge cases:
# one word, two words, just return them as is
# even amount of words: returns the leftmost of the middle words
# zero words: return None
# I'm going to assume we are always given a sentence