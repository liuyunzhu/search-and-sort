def quicksort(array):
    if len(array) == 0:
        return []
    else:
        pivot = array[0]
        less = []
        great = []
        for item in array[1:]:
            if item < pivot:
                less.append(item)
            else:
                great.append(item)

        less = quicksort(less)
        great = quicksort(great)

        return less + [pivot] + great
