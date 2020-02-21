def calc_factorial(x):
    if x == 1:
        return 1
    else:
        return (x*calc_factorial(x-1))
grab = input('Enter a number to find its factorial:')
b=int(grab)
print ('Factorial of',b,'is:',calc_factorial(b))
