''' Implement Heap Data Structure (using Array).
        1. minHeap
        2. maxHeap
'''

def minHeapify(arr, i):
    index = i
    n = len(arr)
    leftChild = 2*i + 1
    rightChild = 2*i + 2
        
    if (rightChild < n) and (arr[index] > arr[rightChild]):
        index = rightChild
                
    if (leftChild < n) and (arr[index] > arr[leftChild]):
        index = leftChild
        
    if index != i:
        arr[index], arr[i] = arr[i], arr[index]
        minHeapify(arr, index)

def maxHeapify(arr, i):
    index = i
    n = len(arr)
    leftChild = 2*i + 1
    rightChild = 2*i + 2
        
    if (rightChild < n) and (arr[index] < arr[rightChild]):
        index = rightChild
                
    if (leftChild < n) and (arr[index] < arr[leftChild]):
        index = leftChild
        
    if index != i:
        arr[index], arr[i] = arr[i], arr[index]
        maxHeapify(arr, index)

def heapify(arr, func = minHeapify):
    n = len(arr) // 2 - 1
    for i in range(n, -1, -1):
        func(arr, i)

def minHeapInsert(arr, item):
    if not arr:
        arr = [item]
        return
    
    arr.append(item)
    i = len(arr) - 1
    parent = (i - 1) // 2
    while parent >= 0:
        if arr[i] < arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent
            parent = (i - 1) // 2
        else:
            break

def minHeapifyDelete(arr):
    delItem = None
    if arr:
        n = len(arr) - 1
        if n == 0:
            delItem = arr.pop(0)
        else:
            delItem = arr[0]
            arr[0] = arr.pop(n)
            minHeapify(arr, 0)
    return delItem
     

if __name__ == '__main__':
    
    # Sample Input Cases
    arr1 = [0,1,2,3,4,5,6,7,8,9]
    arr2 = [9,8,7,6,5,4,3,2,1,0]
    arr3 = [1,6,8,2,5,7,1,6,9,2]
    arr4 = [9,2,6,3,7,1,3,5,6,9]
    arr5 = [6,7,3,4,5,8,9,4,5,2]
    arr6 = [3,6,8,2,7,9,2,1,9,4]
    
    # Selected Input Case
    arr = arr3
    print('Input Array :',arr)
    
    # Execute tests
    
    #heapify(arr, maxHeapify)
    #print('Max Heap :',arr)
    
    heapify(arr, minHeapify)
    print('Min Heap :',arr)
    
    minHeapInsert(arr, 0)
    print('Min Heap Insert :',arr)
    
    minimun = minHeapifyDelete(arr)
    print('Minimum Deleted :', minimun)
    print('Min Heap Delete :', arr)
    
