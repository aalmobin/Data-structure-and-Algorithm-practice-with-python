def fibonacci(n):
    """Calculate the fibonacci series"""
    
    assert n >= 0 and int(n) == n, 'fibonacci number can not be negative or non integers'
    if n in [0,1]:
        return n 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 
n = int(input('Enter integer n to find nth fibonacci series: '))
for i in range(n):
    result = fibonacci(i) 
    print(result,end=" ")