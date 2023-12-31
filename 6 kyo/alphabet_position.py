"""
Given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.

Examples: 

"The sunset sets at twelve o' clock."
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

"""

import string
def alphabet_position(text):
    outS = ''.join([i for i in text if i.isalpha()])
    finalS = ""
    for x in outS:
        finalS1 = string.ascii_lowercase.index( x.lower()) + 1
        finalS = finalS + str(finalS1) + " "
    finalS.strip()
    finalS1 = finalS[:-1]
    return(finalS1)




  
 



