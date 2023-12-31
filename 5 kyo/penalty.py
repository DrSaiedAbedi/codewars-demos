"""
Combine the given numbers such as speed of your car, speed limit in the area, 
speed of the police car chasing you, the number of police cars involved, etc. 
to make the penalty charge to be as small as possible.

Examples:

['45', '30', '50', '1'] => '1304550'
['100', '10', '1'] => '100101'
['32', '3'] => '323'

"""

def penalty(numbers):
    finalResult = ""
    countSuperior = []
    for i in range(len(numbers)):
        countSuperior.append(0)
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                numIJ = str(numbers[i])+str(numbers[j])
                numJI = str(numbers[j])+str(numbers[i])
                if int(numIJ) < int(numJI):
                    countSuperior[i] += 1
                else:
                    countSuperior[j] += 1
    for i in range(len(numbers)):
        max1 = max(countSuperior)
        j = countSuperior.index(max1)
        finalResult += numbers[j]
        countSuperior[j] = -1
    return(finalResult)