def stringy(num):
    result = ''
    for number in range(num):
        if number % 2 == 0:
            result += '1'
        else:
            result += '0'
    return result

def stringy(num):
    bit = '1'
    result = ''

    for _ in range(num):
        result += bit
        if bit == '1':
            bit = '0'
        else:
            bit = '1'
    
    return result

def stringy(number):
    index = 1
    result = ''
    for _ in range(number):
        result += str(index % 2)
        index += 1

    return result

def stringy(num):
    return ''.join([str(digit % 2) for digit in range(1, num + 1)])

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True