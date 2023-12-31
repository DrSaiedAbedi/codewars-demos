"""
Refactor the Fibonacci function into a recursive Fibonacci function that using a 
memoized data structure avoids the deficiencies of tree recursion.

"""

myCache = {0: 0, 1: 1}
def fibonacci(n):
    if n in myCache:  
        return myCache[n]
    myCache[n] = fibonacci(n - 1) + fibonacci(n - 2)  
    return myCache[n]