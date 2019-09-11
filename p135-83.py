def getSubsets(setz, index):
    """
    allsubset for recursion
    base case: size == index
        if {} not in allsubset add empty set
    recursion:
    """
    allsubsets = []
    if len(setz) == index:
        if [] not in allsubsets:
            allsubsets.append([])
    else:
        allsubsets = getSubsets(setz,index+1)
        item = setz[index]
        moresubsets = []
        for subset in allsubsets:
            newSubset = []
            [newSubset.append(value) for value in subset if value not in newSubset]
            newSubset.append(item)
            moresubsets.append(newSubset)
        [allsubsets.append(value) for value in moresubsets if value not in newSubset]
    return allsubsets











    # allSubsets = []
    # if len(setz) == index:
    #     #base case - add empty set
    #     if [] not in allSubsets:
    #         allSubsets.append([])
    # else:
    #     allSubsets = getSubsets(setz, index+1)
    #     print('allsubsets-->',allSubsets)
    #     item = setz[index]
    #     moreSubsets = []
    #     for subset in allSubsets:
    #         print('subset',subset)
    #         newSubset = []
    #         [newSubset.append(value) for value in subset if value not in newSubset]
    #         newSubset.append(item)
    #         print(newSubset)
    #         moreSubsets.append(newSubset)
    #     [allSubsets.append(value) for value in moreSubsets if value not in newSubset]
    # return allSubsets

arr = ['a','b','c']
a = getSubsets(arr,0)
print(a)

