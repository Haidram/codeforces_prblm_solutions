def mergeSortedArray(x,startx,midx,endx):
    temp1 = [0]*(midx-startx+1)
    temp2 = [0]*(endx-midx)
    i = 0
    j = 0
    while i < len(temp1):
        temp1[i] = x[startx+i]
        i += 1
    while j < len(temp2):
        temp2[j] = x[midx+1+j]
        j += 1
    
    i = 0
    j = 0
    k = startx
    while i < len(temp1) and j < len(temp2):
        if temp1[i] < temp2[j]:
            x[k] = temp1[i]
            i += 1
        else:
            x[k] = temp2[j]
            j += 1
        k += 1
        
    while i < len(temp1):
        x[k] = temp1[i]
        i += 1
        k += 1
    
    while j < len(temp2):
        x[k] = temp2[j]
        j += 1
        k += 1
    
def sortArray(a,start,end):
    if end > start: 
        mid = int((end+start)/2)
        sortArray(a,start,mid)
        sortArray(a,mid+1,end)
        mergeSortedArray(a,start,mid,end)

numArray = list(map(int,input().strip().split()))[:8]
sortArray(numArray,0,7)
print(numArray)
