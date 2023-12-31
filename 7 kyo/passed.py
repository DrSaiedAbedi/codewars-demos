"""
To calculate the average demerit points accumulated by ONLY the 
students who have passed driving test, rounded to the nearest integer.

Example:

[10,10,10,18,20,20] --> 12

"""

def passed(lst):
    sumPoints = 0
    numCountable = 0
    for x in lst:
        if x <= 18:
            sumPoints= sumPoints + x
            numCountable = numCountable + 1
    if sumPoints == 0:
        return('No pass scores registered.')
    else:
        return(round(sumPoints/numCountable))