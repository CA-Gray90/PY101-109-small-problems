def multiply(a, b):
    return a * b

def square(number):
    return multiply(number, number)

print(square(5) == 25)
print(square(6) == 36)
print(square(-2) == 4)

# def power(base, n):   # 2, 4 = 16
#     result = 1
#     for _ in range(n):
#         result = multiply(result, base)

#     return result

# Other students solution:

def power_to_n(base, power):    # 2, 5
    result = 1

    # Adjust for odd exponents
    if power % 2 != 0: 
        result = base  # 2
        power -= 1 # 4


    for _ in range(power // 2): # 2, 0 - 1
        result *= multiply(base, base)

    return result

print(power_to_n(2, 5) == 32)
print(power_to_n(2, 6) == 64)
    