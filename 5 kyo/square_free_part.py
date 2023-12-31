"""
A function which accepts a number n and returns the squarefree part of n.

Examples:

 2  ---> 2
 4  ---> 2
 24 --->  6 (since any larger divisor is divisible by 4, which is a square)

"""

def square_free_part(n):
    import math
    squareDs = []
    noSquareDs = []
    for i in range(1, n):
        j = i + 1
        if n % j == 0 and j != int(math.sqrt(j))*int(math.sqrt(j)):
            noSquareDs.append(j)
        if n % j == 0 and j == int(math.sqrt(j))*int(math.sqrt(j)):
            squareDs.append(j)
    eliminateWithSqs = []
    for i in range(len(noSquareDs)):
        eliminateWithSqs.append(False)
    k = 0
    for x in noSquareDs:
        for y in squareDs:
            if x % y == 0:
                eliminateWithSqs[k] = True
        k += 1
    finalRes = -1
    m = 0
    for i in range(len(eliminateWithSqs)):
        if not(eliminateWithSqs[i]) and noSquareDs[i] > finalRes:
            finalRes = noSquareDs[i]
    if finalRes == -1:
        finalRes = n
    return(finalRes)