import time
def middle_of_three(arr, low, hi):#midian of three
    mid = (low + hi) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[mid] > arr[hi]:
        arr[mid], arr[hi] = arr[hi], arr[mid]
    if arr[mid] < arr[low]:
        arr[low], arr[mid] = arr[mid], arr[low]
    return mid

def swap(array,a,b): #swapping 
    array[a],array[b] = array[b],array[a]
    
def partition(array,start,end):
    median = middle_of_three(array,start,end)#pivot using median of three
    left = start + 1
    if (array[median] - array[end-1])*(array[start]-array[median]) >= 0:
        swap(array,start,median)
    elif (array[end - 1] - array[median]) * (array[start] - array[end - 1]) >=0:
         swap(array,start,end - 1)
    pivot = array[start] 
    for right in range(start,end):
        if pivot > array[right]:
            swap(array,left,right)
            left = left + 1
    swap(array,start,left-1)
    return left-1

def quickSortR(array,start,end):#quicksort
    if start < end:
        split = partition(array,start,end)
        quickSortR(array,start,split)#calling recursively
        quickSortR(array,split+1,end)
        
def QuickSort(array):
    quickSortR(array,0,len(array)-1)
    
L = input("Input: ")
X = [int(e) for e in L.split(',')]
start = time.time()
QuickSort(X)
stop = time.time()
elapse = stop - start
print("Time spent", elapse)
