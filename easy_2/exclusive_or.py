def xor(operand_1, operand_2):
    elements = [operand_1, operand_2]

    return False if all(elements) else any(elements)

    # if (operand_1 and not operand_2) or (operand_2 and not operand_1):
    #     return True
    # else:
    #     return False

# def xor(x,y): 
#     return bool(x) != bool(y)

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
print(xor(False, []) == False)

# Further exploration
# Situation in which a boolean xor would be useful?
# Penumatic piston with air pipes flowing into either end of the piston. To get
# movement you want air flowing into one pipe only, not both?

# Does my xor function perform short circuit evaluation? I need to look at the 
# documentation for any() and whether that performs short circuiting. 
# According to the python docs, any() is equivalent to:

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

# This function will terminate and return True as soon as it encounters a
# truthy variable, therefore, in a way, it does indeed do short-circuiting since it
# not evaluate any other elements after encountering a truthy element.
# However, since we are first evaluating both elements with all(), overall my
# function does not exhibit short-circuiting. In the case of an xor, both 
# elements must be evaluated to get the right result. 