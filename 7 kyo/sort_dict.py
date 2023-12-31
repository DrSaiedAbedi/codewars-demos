"""
Create a function that returns a sorted list of (key, value) 
tuples out of an inherently unsorted Python dictionary.

Example:

sort_dict({3:1, 2:2, 1:3}) == [(1,3), (2,2), (3,1)]
sort_dict({1:2, 2:4, 3:6}) == [(3,6), (2,4), (1,2)]

"""

def sort_dict(d):
    sorted_d = sorted(d.items(), key = lambda x:x[1], reverse=True)
    converted_dict = dict(sorted_d)
    resultList = list(converted_dict.items())
    finalList = []
    for x in resultList:
        finalList.append(tuple(x)) 
    return(finalList)