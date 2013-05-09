def linearsearch(array,target):
    for i in range(0,len(array)):
        if array[i] == target:
            return i
    return -1
