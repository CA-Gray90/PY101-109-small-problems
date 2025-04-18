# Create a function that takes an array of objects as argument and return the
# same array with all the elements sorted according to it's value in ascending
# order. 

def sorting(lst):
    
    def get_value(dictionary):
        value = list(dictionary.values())
        return value[0]

    lst.sort(key=get_value)
    return lst

print(sorting([{'a': 1}, {'a': 0}, {'a': 3}])) # => [{a:0}, {a:1}, {a:3}]