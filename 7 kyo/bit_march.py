"""
n bits march from right to left along an 8 bits path. Once the 
most-significant bit reaches the left their march is done. Each 
step will be saved as an array of 8 integers.
Example: 

n = 3

Returns:

00000111
00001110
00011100
00111000
01110000
11100000
"""

def bit_march (n : int) -> list:
    m = 2**n - 1
    bM = format(m,'08b')
    bMArr = list(bM)
    outputL = []
    k = m
    bM1 = format(k,'08b')
    bMArr1 = list(bM1)
    bMArrI = []
    for x in bMArr1:
        bMArrI.append(int(x))
    outputL.append(bMArrI)
    
    nLoop = 8 - n
    for i in range(nLoop):
        k = m << 1
        bM1 = format(k,'08b')
        bMArr1 = list(bM1)
        bMArrI = []
        for x in bMArr1:
            bMArrI.append(int(x))
        outputL.append(bMArrI)
        m = k
    return(outputL)




  
 



