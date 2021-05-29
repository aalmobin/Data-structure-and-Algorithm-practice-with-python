def gcd(a, b):
    """Finding the greatest common divisor"""
    
    assert int(a) == a and int(b) == b, 'The numbers must be integers only'
    if a < 0:
        a = -1*a
    if b < 0:
        b = -1*b
    if b == 0:
        return a 
    else:
        return gcd(b, a%b)
        
a = int(input('Enter the first number: '))
b = int(input('Enter the 2nd number: '))
print(gcd(a,b))
