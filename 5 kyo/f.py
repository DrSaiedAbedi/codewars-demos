"""

Find the closest prime number under a certain integer n that has
 the maximum possible amount of even digits.

Example;

f(1000) ---> 887 (even digits: 8, 8)
f(1210) ---> 1201 (even digits: 2, 0)
f(10000) ---> 8887
f(500) ---> 487
f(487) ---> 467

"""

def f(n):
      s = str(n)
      s1 = s[-1:0]
      sumS1 = 0
      for x in s1:  
        sumS1 = sumS1 + int(x)
      sFirst = s[0]
      sFirstN = int(sFirst)
      flagTens = False
      if (sFirstN == 1)&(sumS1 == 0):
        flagTens = True
      lenS = len(s)
      s = s[:-1]
      nNext = int(s)
      n_nextSave = 0
      numEvenDigits = 0
      numModeZ2 = 0
      flagFirstVisit = False
      while(numEvenDigits < lenS-2)|(numModeZ2 != 1):      
        numDigits = 0
        str_m_down = str(nNext)
        lenCheck = len(str_m_down)
        for x in str_m_down:  
          if int(x) % 2 == 0:
            numDigits  = numDigits  + 1

        if numDigits < lenS -1 or not(flagFirstVisit):
          nNext = nNext - 1
        else:
          flagFirstVisit = True
        n_nextSave = nNext
        s = str(n)
        s1 = s[-1:0]
        sumS1 = 0
        for x in s1:  
          sumS1 = sumS1 + int(x)
        sFirst = s[0]
        sFirstN = int(sFirst)
        flagTens = False
        if (sFirstN == 1)&(sumS1 == 0):
          flagTens = True
        numDigits = 0
        str_m_down = str(nNext)
        lenCheck = len(str_m_down)
        for x in str_m_down:  
          if int(x) % 2 == 0:
            numDigits  = numDigits  + 1
        if flagTens:
          if numDigits >= lenS - 2:
            numEvenDigits = numDigits
            tailNum = [9, 7, 3, 1]
            for x in tailNum:
              SaNum = str(n_nextSave)+str(x)
              aNum = int(SaNum)
              if aNum < n:
                numModeZ = 0
                for j in range(aNum-1):
                  if (aNum % (j+1) == 0):
                    numModeZ = numModeZ + 1
                numModeZ2 = numModeZ
                if numModeZ == 1:
                  break
        else:
          if numDigits >= lenS - 1:
            numEvenDigits = numDigits
            tailNum = [9, 7, 3, 1]
            for x in tailNum:
              SaNum = str(n_nextSave)+str(x)
              aNum = int(SaNum)
              if aNum < n:
                numModeZ = 0
                for j in range(aNum-1):
                  if (aNum % (j+1) == 0):
                    numModeZ = numModeZ + 1
                numModeZ2 = numModeZ
                if numModeZ == 1:
                  break
      tailNum = [9, 7, 3, 1]
      maxFound = 0
      for x in tailNum:
        SaNum = str(n_nextSave)+str(x)
        aNum = int(SaNum)
        if aNum <= n: 
          numModeZ = 0
          for j in range(aNum-1):
            if (aNum % (j+1) == 0):
              numModeZ = numModeZ + 1
          if numModeZ == 1:
            if aNum > maxFound:
              maxFound = aNum
      return(maxFound)