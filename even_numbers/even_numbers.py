# Print all numbers from 1 - 99 inclusive

# for i in range(1, 100):
#     if i % 2 == 0:
#         print(i)

# for i in range(2, 100, 2):
#     print(i)

# Writing it as a function that takes two arguments:

def print_even_nums(start, end):
    if start % 2 != 0:
        start += 1
    for i in range(start, end + 1, 2):
        print(i)

print_even_nums(1, 99)
print()
print_even_nums(-3, 20)
print()
print_even_nums(0, 2)
print()
print_even_nums(0, 0)
print()
print_even_nums(0, 1)