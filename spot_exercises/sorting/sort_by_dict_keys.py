# Create a function that takes an array of objects as argument and return the
# same array with all the elements sorted according to it's key in descending order.

def sorting(lst):

    def get_key(dictionary):
        key = list(dictionary)
        return key[0]

    lst.sort(key=get_key, reverse=True)
    return lst

# PCODE:
# Access dict, access key, sort according to key
# define a function that accesses the key of a dict and returns it
# use this in sort?

# For example:
print(sorting([{0: 1}, {3: 1}, {1 : 1}])) # => [{3:1}, {1:1}, {0:1}]

# key = [key for key in {0: 1}.keys()]
# print(key[0])