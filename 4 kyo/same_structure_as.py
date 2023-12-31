"""
Complete the function/method (depending on the language) to return true/True
 when its argument is an array that has the same nesting structures and same 
 corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )
"""

def same_structure_as(original,other):
    import re
    #Replacing non-digit conents with digits 
    aOr = str(original)
    res = re.findall(r'\'.*?\'', aOr)
    for x in res:
        aOr = aOr.replace(x,"0")
    aOo = str(other)
    res = re.findall(r'\'.*?\'', aOo)
    for x in res:
        aOo = aOo.replace(x,"0")
    original = list(aOr)
    other = list(aOo)
    if original.__class__ == list:
        if (len(original) == 0):
            original = []
            strOriginal = ''.join(map(str, list(original)))
        else:
            strOriginal = ''.join(map(str, list(original)))
    else:
        strOriginal = str(original)
    strOriginal = '[' +  strOriginal
    strOriginal = strOriginal + ']'
    if other.__class__ == list:
        if (len(other) == 0):
            strOther = []
            strOther = ''.join(map(str, list(other)))
        else:
            strOther = ''.join(map(str, list(other)))
    else:
        strOther = str(other)
    strOther = '[' + strOther
    strOther = strOther + ']'
    for ele in strOriginal:
        if ele.isnumeric():
            strOriginal =  strOriginal.replace(ele, '0')
    strOriginal = strOriginal.replace("-", "" )
    char = '0'
    pattern = char + '{2,}'
    strOriginal = re.sub(pattern, char, strOriginal)
    for ele in strOther:
        if ele.isnumeric():
            strOther =  strOther.replace(ele, '0')
    strOther = strOther.replace("-", "" )
    strOther = re.sub(pattern, char, strOther)  
    if (strOriginal == strOther):
        return(True)
    else:
        return(False)