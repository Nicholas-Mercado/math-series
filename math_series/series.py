

def sum_series(n, arg1=0, arg2=1):
    """
    Calls either Default: Fibonacci or Lucas depending on optional parameters

    Parameters:
    Argument 2-3 (int): (n) = default Fibonacci(), (n,2,1) = invokes Lucas()
    
    """
    
    if n < 0:
        return "Cannot compute"
    elif n == 0:
        return arg1
    elif n == 1:
        return arg2
    elif n > 1:
        return sum_series(n-1, arg1, arg2) + sum_series(n-2, arg1, arg2)


def Fibonacci(n):

    if n < 0:
        return "Cannot compute"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return Fibonacci(n-1) + Fibonacci(n-2)


def Lucas(n):

    if n < 0:
        return "Cannot compute"
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        return Lucas(n-1) + Lucas(n-2)
