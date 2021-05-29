def factorial(n):
    """Calculate the factorial of an integer number"""
    
    assert n >= 0 and int(n) == n,'Number must be positive integers only'
    if n in [0,1]:
        return 1 
    else:
        return n * factorial(n-1)
        
n = int(input('Enter a positive integer to find factorial: '))
result = factorial(n)
print(f'{n}! = {result}')