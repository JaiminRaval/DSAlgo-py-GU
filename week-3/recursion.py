
def factorial(n):
    if n == 0:
        print(n)
        return 1
    else:
        print(n)
        return n * factorial(n - 1)
