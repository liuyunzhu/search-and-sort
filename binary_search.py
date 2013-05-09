def binarysearch(array,target,low,high):
    mid = (low + high)//2
    if low > high:
        return -1
    elif array[mid] == target:
        return mid
    elif array[mid]<target:
        return binarysearch(array,target,mid+1,high)
    else:
        return binarysearch(array,target,low,mid-1)

