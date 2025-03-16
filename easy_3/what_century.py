# Write a function that takes a year as input and returns the century. The
# return value should be a string that begins with the century number, and ends
# with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

# New centuries begin in years that end with 01. So, the years 1901 - 2000
# comprise the 20th century.

def century(year):
    century_year = str(year // 100 if year % 100 == 0 else (year // 100) + 1)

    suffix_dict = {
        '1' : 'st',
        '2' : 'nd',
        '3' : 'rd',
        ('4', '5', '6', '7', '8', '9', '0') : 'th'
    }

    if len(century_year) > 1 and century_year[-2] == '1':
        suffix = 'th'
    else:
        for key in suffix_dict.keys():
            if century_year[-1] in key:
                suffix = suffix_dict[key]
    
    return f'{century_year}{suffix}'

def century(year):
    century_year = str(year // 100 if year % 100 == 0 else (year // 100) + 1)

    suffix_dict = {
        '1' : 'st',
        '2' : 'nd',
        '3' : 'rd',
        ('4', '5', '6', '7', '8', '9', '0') : 'th'
    }

    if century_year.endswith(('11', '12', '13')):
        suffix = 'th'
    else:
        for key in suffix_dict.keys():
            if century_year[-1] in key:
                suffix = suffix_dict[key]
    
    return f'{century_year}{suffix}'

def century(year):
    century_year = str(year // 100 if year % 100 == 0 else (year // 100) + 1)

    if century_year.endswith(('11', '12', '13')):
        suffix = 'th'
    else:
        match century_year[-1]:
            case '1':
                suffix = 'st'
            case '2':
                suffix = 'nd'
            case '3':
                suffix = 'rd'
            case _:
                suffix = 'th'
    
    return f'{century_year}{suffix}'

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
print(century(503) == "6th")            # True