def repeat(text, multiplier):
    if multiplier > 0:
        for _ in range(multiplier):
            print(text)
    else:
        print('Multiplier must be greater than 0')

repeat('Hello', 3)
repeat('Hello this is a longer sentence', 5)
repeat('Hello', 0)
repeat('Hello', -3)