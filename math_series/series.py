def sum_series(n, num=0, num_two=1):

    if num == 0 and num_two == 1:
        return Fibonacci(n)
    if num == 1 and num_two == 2:
        return Lucas(n)
         


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
