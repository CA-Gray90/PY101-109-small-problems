# Create a function that takes a string as an argument and returns a number
# representing number of words that occurred more than once in that string, 
# for example:

# count_duplic('one two one three two'); //=> 2
# count_duplic('flower cat cat dog flower dog'); //=> 3

def count_duplic(string):
    list_of_words = string.split()
    result = []

    for word in list_of_words:
        if list_of_words.count(word) > 1 and (word not in result):
                result.append(word)

    return len(result)

print(count_duplic('one two one three two')) # ; //=> 2
print(count_duplic('flower cat cat dog flower dog')) # ; //=> 3
print(count_duplic('banana kiwi kiwi kiwi kiwi apple apple cherry')) # ; //=> 2

# PSEUDOCODE:
# get a list of words using .split()
# get a set constructed from the list of words
# counter = 0
# iterate through the set. 
# for each element in the set, get the count of that word in the list.
# if that count is greater than 1, incremenet counter += 1
# return counter