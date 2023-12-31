"""
Given an array of positive or negative integers

 I= [i1,..,in]

the code should produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers.

Example:
I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]

"""

primeLst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def sum_for_list(ls):
    memList = []
    for x in ls:
        primeDivisors = []
        firstList =[]
        n = abs(x)
        for h in primeLst:
            if n % h == 0:
                n = n / h
                n = int(n)
                firstList.append(h)  
        prime_factors = lambda n: [i for i in range(2, n+1) if n%i == 0 and all(i % j != 0 for j in range(2, int(i**0.5)+1))]
        factors = []
        while n > 1:
            for factor in prime_factors(n):
                factors.append(factor)
                n //= factor
        primeDivisors =  firstList + factors
        primeDivisors = list(dict.fromkeys(primeDivisors))
        for yPrime in primeDivisors:
            flagExist = False 
            for j in range(len(memList)):
                if memList[j][0] == yPrime:
                    memList[j][1] = memList[j][1] + x 
                    flagExist = True
            if not(flagExist):
                memList.append([yPrime, x])
    return(sorted(memList,key=lambda x: (x[0])))