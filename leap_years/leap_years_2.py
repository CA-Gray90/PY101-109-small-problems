# Write a program that displays whether a given year is a leap year, observing
# the change from the julian calender to the gregorian calender in various
# regions of the world

EU = 1582
UK = 1752
JP = 1873
RU = 1918
CH = 1949
SA = 2016

regions_dict = {
    'eu' : ['the majority of Europe', EU],
    'uk' : ['the UK including its colonies and America', UK],
    'jp' : ['Japan', JP],
    'ru' : ['Russia', RU],
    'ch' : ['China', CH],
    'sa' : ['Saudi Arabia', SA]
}

def display_welcome():
    print('This program will display whether a given year was a leap year, as'
        ' determined by region, dependant on when they adopted the Gregorian '
        'calendar. Results and regions are limited.')
    print()
    print('Here are the region options to choose from:')
    for key, value in regions_dict.items():
        print(f'{key} : {value[0]}, adopted in {value[1]}')
    print()
    
def get_region():
    print("Please enter 'eu' for Europe, 'uk' for UK and its colonies, etc.")
    input_region = input().lower()

    while True:
        if input_region in regions_dict:
            break
        print('Please enter a valid region:')
        input_region = input().lower()

    return input_region

def get_year():
    print('Please enter the year:')
    input_year = input()

    while True:
        try:
            input_year = int(input_year)
        except ValueError:
            print('Please enter a whole number:')
            input_year = input()
        else:
            break

    return input_year

def gregorian_calendar(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def julian_calendar(year):
    return year % 4 == 0

def is_leap_year(year, region):
        if year >= regions_dict[region][1]:
            return gregorian_calendar(year)
        return julian_calendar(year)

def display_result(year, region, result):
    result_dict = {True : 'a leap year.', False : 'not a leap year.'}

    print(f'In {regions_dict[region][0]}, the year {year} was '
          f'{result_dict[result]}')

display_welcome()
user_region = get_region()
user_year = get_year()
result = is_leap_year(user_year, user_region)
display_result(user_year, user_region, result)