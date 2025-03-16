# Write a function that takes `n` (an integer) as argument and returns a triangle
# of stars with height `n` and length `n`:

# eg:
# triangle(4):

#    *
#   **
#  ***
# ****

def triangle(n):
    for num in range(1, n + 1):
        print(f'{('*' * num).rjust(n)}')

triangle(5)
triangle(0)
triangle(20)
triangle(-3)
triangle(1)