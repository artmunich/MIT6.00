def selSort(L):
    for i in range(len(L)-1):
        minIndex = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndex = j
                minVal = L[j]
            j += 1
        temp = L[i]
        L[i] = minVal
        L[minIndex] = temp