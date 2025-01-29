# Write a function that takes one integer argument and returns True when
# the numbers absolute value is odd, False otherwise

# Pseudocode:
# - Define a function `is_odd`` that takes one argument, `n`, an integer
# - Check whether the absolute value of `n` is odd. I.e. if there is a 
# remainder when `n` is divided by 2, then it is said to be odd.
# - If it is odd, return `True` ,(Boolean value) else return `False`

# Formal Pseudocode:
# DEF a function; is_odd(n)
# IF abs(n) is odd
#   RETURN `TRUE`
# ELSE:
#   RETURN `FALSE`

# def is_odd(n):
#     if n % 2 == 1:
#         return True
#     else:
#         return False

# def is_odd(n):
#     return True if n % 2 else False

# More readable Ternary expression:

def is_odd(n):
    return True if n % 2 == 1 else False

# LS Solution:
# Clear intent using abs() (it was in the request), the expression will return
# a boolean, which is then returned by the function. Succint code.

def is_odd(n):
    return abs(n) % 2 == 1


print(is_odd(3))    # True
print(is_odd(4))    # False 
print(is_odd(13))   # True
print(is_odd(0))    # False
print(is_odd(-10))   # False
print(is_odd(-1000002))   # False
print(is_odd(-1))   # True