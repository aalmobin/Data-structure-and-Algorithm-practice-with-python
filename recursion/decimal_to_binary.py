def decimalTobinary(n):
    """Convert a decimal number to binary"""
    
    assert int(n) == n, 'input number must be integer'
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimalTobinary(int(n/2))

n = int(input('Enter a decimal number: '))
result = decimalTobinary(n)
print(f'The binary value of {n} is {result}')