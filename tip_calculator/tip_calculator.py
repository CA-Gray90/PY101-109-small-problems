# Create a simple tip calculator. The program should prompt for a bill amount
# and a tip rate. The program must compute the tip, then print both the tip and
# the total amount of the bill. You can ignore input validation and assume that
# the user will enter valid numbers.

print('Welcome to the tip calculator!')
bill = float(input('What is the bill? '))
tip_percentage = float(input('What is the tip percentage? '))

tip = tip_percentage * (bill / 100)

print(f'The tip is ${tip:.2f}')
print(f'The total bill is ${tip + bill:.2f}')