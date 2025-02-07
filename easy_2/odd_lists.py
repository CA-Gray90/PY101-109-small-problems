# Write a function that returns a list that contains every other element of a
# list that is passed in as an argument. Use list slicing

# def oddities(seq):
#     index = 1
#     result = []
#     for item in seq:
#         if index % 2 != 0:
#             result.append(item)
#         index += 1

#     return result

# def oddities(seq):
#     result = []
#     for index in range(0, len(seq), 2):
#         result.append(seq[index])

#     return result

def oddities(seq):
    return seq[::2]

# Bonus question:

def evens(seq):
    result = []
    for index in range(1, len(seq), 2):
        result.append(seq[index])

    return result

def evens(seq):
    return [seq[index] for index in range(1, len(seq), 2)]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

print(evens([2, 3, 4, 5, 6, 7]) == [3, 5, 7])    # True
print(evens([1, 2, 3, 4]) == [2, 4])             # True
print(evens(["abc", "def"]) == ['def'])          # True
print(evens([123]) == [])                        # True
print(evens([]) == [])                           # True