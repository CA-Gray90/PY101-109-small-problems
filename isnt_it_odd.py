# Write a function that takes one integer argument and returns True when the
# number's absolute value is odd, False otherwise.

def is_odd(n):
    return n % 2 != 0

print(is_odd(5))    # True
print(is_odd(2))    # False
print(is_odd(-2))   # False
print(is_odd(-23))  # True