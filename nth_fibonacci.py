# nth fib is the sum of (n - 1) and (n - 2)
# function should take in an int `n` and return the `nth` fibonacci number
def getNthFib(n):
    fibs = {0: 0, 1: 1, 2: 1}
    findNthFib(n, fibs)

def findNthFib(n, fibs):
    possibleMatch = fibs.get(n)
    if possibleMatch is not None:
        return fibs[n]
    else:
        fibs[n] = findNthFib(n - 1, fibs) + findNthFib(n - 2, fibs)

    return fibs[n]
