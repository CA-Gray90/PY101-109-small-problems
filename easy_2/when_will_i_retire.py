from datetime import date

CURRENT_YEAR = date.today().year

def get_user_age():
    age = input('What is your age? ')

    while True:
        try:
            age = int(age)
            if age <= 0:
                raise ValueError
        except ValueError:
            print('Please enter a positive whole number:')
            age = input()
        else:
            return age

def get_retirement_age(current_age):
    retire_age = input('At what age would you like to retire? ')

    while True:
        try:
            retire_age = int(retire_age)
            if retire_age < current_age:
                raise ValueError
        except ValueError:
            print('Invalid age, please try again using whole numbers greater '
                  'than your current age:')
            retire_age = input()
        else:
            return retire_age

def calculations(current_year, age, retirement_age):
    years_to_go = retirement_age - age
    retirement_year = current_year + years_to_go
    return (years_to_go, retirement_year)

def main():
    user_age = get_user_age()
    retirement_age = get_retirement_age(user_age)
    years_left, retirement_year = calculations(CURRENT_YEAR, user_age, retirement_age)

    print(f'It is {CURRENT_YEAR}. You will retire in {retirement_year}.')
    if years_left == 0:
        print(f'You will retire this year! Congrats!')
    else:
        print(f'You have only {years_left} years to go!')

main()