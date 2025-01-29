# Write a function that computes the sum of all numbers between 1 and some
# other number, inclusive, that are multiples of 3 or 5. 

def multisum(number):
    nums_list = [num for num in range(1, number + 1)\
                 if num % 3 == 0 or num % 5 == 0]
    return sum(nums_list)

print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)