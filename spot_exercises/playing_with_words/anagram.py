# An anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.

# Create a function that takes two strings as arguments and returns a boolean
# value if the two words are anagrams and false if they are not anagrams.
# For example:

def is_anagram(word_1, word_2):
    word_1_list = [char for char in word_1]
    word_2_list = [char for char in word_2]

    word_1_list.sort()
    word_2_list.sort()

    return word_1_list == word_2_list

# check whether the length of each word match
#   if len(word1) == len(word2):
# check whether the characters in each word appear the exact same amount of
# times
# define two lists for each word containing a list of characters from that word
# using list comprehensions
# sort both the lists
# compare the lists using value comparison `==`

# return boolean


print(is_anagram('aba', 'aab')) # true
print(is_anagram('aba', 'aa')) # false
print(is_anagram('abadef', 'abbcca')) # false