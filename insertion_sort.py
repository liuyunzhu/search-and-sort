def insertionsort(a):
    for j in range(1,len(a)):
        num = a[j]
        i = j -1
        while (i>= 0 and a[i]>num):
            a[i+1] = a[i]
            i = i -1
        a[i+1] = num
    return a
