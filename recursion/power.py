def power(base, exp):
    """Finding the power"""
    
    assert exp >=0 and int(exp) == exp, 'The exponential must be positive integers only'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base, exp-1)

base = int(input('Enter the base: '))
exp = int(input('Enter the exponential: '))    
print(power(base,exp))