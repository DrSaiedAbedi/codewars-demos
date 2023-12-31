"""

Create a code to count all the permutations for an array of certain length.

Example;

arr = [1, 2, 3, 4]
      (2, 1, 4, 3)
      (2, 3, 4, 1)
      (2, 4, 1, 3)
      (3, 1, 4, 2)
      (3, 4, 1, 2)
      (3, 4, 2, 1)
      (4, 1, 2, 3)
      (4, 3, 1, 2)
      (4, 3, 2, 1)
      _____________
      
A total of 9 permutations with all their elements in different positions than arr

"""

def all_permuted(array_length):
    import itertools
    n = array_length
    finP = []
    pureFinP = []
    iIndex = []
    for i in range(4):
        iIndex.append(i+1) 
        i1 = i + 1
        baseArray = []
        for j in range(i1):
            baseArray.append(j+1)
        perm = list(itertools.permutations(baseArray, i1))
        refinePerm = []
        for x1 in perm:
            x = list(x1)
            compPerm = []
            for j in range(i1):
                compPerm.append(x[j] - (j+1))
            #print(compPerm)
            if not(0 in compPerm):
                refinePerm.append(x)    
        finRes = len(refinePerm)
        if i > 1:
            pFinRes = finRes/i
        else:
            pFinRes = 0
        finP.append(int(finRes))
        pureFinP.append(int(pFinRes))
    if (n <= 4):
        return(finP[n-1])
    else:
        nSteps = n - 4
        aNewPureFinP = 0
        for p in range(nSteps):
            iIndex.append(4+p+1)
            aNewPureFinP = pureFinP[4+p-1]*iIndex[4+p-1] - finP[4+p-2-1]
            pureFinP.append(aNewPureFinP)
            finP.append(aNewPureFinP * (4+p))
        return(aNewPureFinP * (n-1))