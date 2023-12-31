"""
Given a binary tree:

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
the task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

Return empty list if root is None.

Example 1 - following tree:

                 2
            8        9
          1  3     4   5
          
Should return following list:

[2,8,9,1,3,4,5]
"""

class Node(object):
    def __init__(self, L, R, n):
        self.value = n
        self.left = L
        self.right = R


def getMyNodes(node, level, arrAll, flagRorL):
    if node != None:
        if (node.value not in arrAll):
            arrAll.append([node.value, level, flagRorL])
        getMyNodes(node.left, level + 1, arrAll,0)
        getMyNodes(node.right, level + 1, arrAll, 1)
    return(arrAll)  

def getTreeDetail(node, level):
    arrAll = []
    finArrAll = []
    arrAll = getMyNodes(node, level, arrAll,-1)
    for i in range(len(arrAll)+level):
        finArrAll.append([i])  
    
    for i in range(len(arrAll)):
        if len(arrAll[i]) < len(arrAll):
            if len(arrAll[arrAll[i][1]])>= 2:
                if arrAll[arrAll[i][1]][2] == 0:
                    finArrAll[arrAll[i][1]].append(arrAll[i][0])
                if arrAll[arrAll[i][1]][2] == 1:
                    finArrAll[arrAll[i][1]].append(arrAll[i][0])
    finAll = []
    for x in finArrAll:
        if len(x) > 1:
            for i in range(1, len(x)):
                finAll.append(x[i])
    if(level==1) and len(finAll) ==0:
        finAll = []
        for i in range(len(arrAll)):
            finAll.append(arrAll[i][0])
        return(finAll)
      
    return(finAll)



def tree_by_levels(node):
    if node == None:
        return([])
    level = 1
    return(getTreeDetail(node, level))