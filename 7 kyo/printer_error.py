"""
A function printer_error which given a string will return 
the error rate of the printer as a string representing a 
rational whose numerator is the number of errors and the 
denominator the length of the control string.

Examples: 

s="aaabbbbhaijjjm"
printer_error(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"

"""

def printer_error(s):
    errorChs = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    printCls = []
    #Creating the list of characters from the control message
    for letter in s:
        printCls.append(letter)
    numErrors = 0
    #Finding the cross section
    for x in printCls:
        for y in errorChs:
            if x == y:
                numErrors = numErrors + 1
    return(str(numErrors)+"/"+str(len(printCls)))




  
 



