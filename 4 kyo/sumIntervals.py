"""
Write a function called sumIntervals/sum_intervals that accepts an array of
 intervals, and returns the sum of all the interval lengths. Overlapping 
 intervals should only be counted once.
 
 Examples:
sumIntervals( [
   [1, 2],
   [6, 10],
   [11, 15]
] ) => 9

sumIntervals( [
   [1, 4],
   [7, 10],
   [3, 5]
] ) => 7

"""
def sum_of_intervals(intervals):
    intTagged = []
    flagOLap = []
    for i in range(len(intervals)):
        intTagged.append(intervals[i][0])
        intTagged.append(intervals[i][1])
    for i in range(len(intTagged)):
        flagOLap.append(0)
    for i in range(len(intTagged)):
        for j in range(len(intervals)):
            if intTagged[i] >= intervals[j][0] and intTagged[i] <= intervals[j][1]:
                flagOLap[i] += 1
    startE = min(intTagged)
    endE = max(intTagged)
    finalRes = 0;
    j = 0
    for i in range(len(intervals)):
        if flagOLap[j] == 1 and intervals[i][0] != startE:
            finalRes = finalRes - intervals[i][0]
        j += 1
        if flagOLap[j] == 1 and intervals[i][1] != endE:
            finalRes = finalRes + intervals[i][1]
        j += 1
    finalRes = finalRes + endE - startE
    return(finalRes)
