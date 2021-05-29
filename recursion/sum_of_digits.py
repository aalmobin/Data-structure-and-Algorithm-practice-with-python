def sumofDigits(n):
    """calculate the sum of the digits of an input integer"""
    
    assert n >= 0 and int(n) == n, 'The number has to be positive integers only'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofDigits(int(n/10))
        
n = int(input('Enter an integer: '))
result = sumofDigits(n)
print(f'The sum of the digits of {n} = {result}')