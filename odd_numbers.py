# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.
# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

print("Let's print all the odd numbers between two other numbers (inclusive).")
start = int(input('Enter a starting number: '))
end = int(input('Enter the end number: '))

if start % 2 == 0:  # if start is an even number, rounds up to first odd number
    start += 1

for num in range(start, end + 1, 2): # iterates only over the odd numbers
    print(num)
