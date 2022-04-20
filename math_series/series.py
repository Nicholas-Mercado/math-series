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
