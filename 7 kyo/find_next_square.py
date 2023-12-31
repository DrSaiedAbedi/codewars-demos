"""
Find the next perfect square! Return the next square if sq is a square, -1 otherwise

Examples: 

121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square

"""

def find_next_square(sq):
    import math
    aRoot = math.sqrt(sq)
    if (aRoot % 1 == 0):
        return(int((aRoot+1)*(aRoot+1)))
    else:
        return(-1)




  
 



