def selectionSort(L):
    n = len(L)
    for i in range(n):
        minVal = L[i]
        for j in range(i+1,n):
            if minVal > L[j]:
                minVal = L[j]
                minIndex = j
        if L[i] > minVal:
            temp = minVal
            minVal = L[i]
            L[i] = temp
        L[minIndex] = minVal
    return L
