def bubbleSort(alist):
    for passNum in range(len(alist)-1,0,-1):
        for i in range(passNum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

#input whatever list you want to sort
alist = [36, 78, 12, 35, 26, 90, 85, 1, 19, 7, 45, 16, 3, 10, 21]
bubbleSort(alist)
print(alist)
