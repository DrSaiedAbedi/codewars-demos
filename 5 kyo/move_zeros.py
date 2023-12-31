"""
Write an algorithm that takes an array and moves all of the zeros to 
the end, preserving the order of the other elements.

Example:
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

"""

def move_zeros(lst):
    import numpy as np
    aList = np.array(lst)
    aLen = len(aList)
    aList = np.delete(aList, np.where(aList == 0)[0])
    fList = np.array(np.zeros(aLen - len(aList)))
    fList1 = fList.tolist()
    intlist = np.array(fList1 ).astype(int).tolist()
    aList1 = aList.tolist()
    lst = aList1 + intlist
    return(lst)