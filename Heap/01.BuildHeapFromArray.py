
def buildHeap(arr):
    last_non_leaf_node = len(arr)//2 -1
    for i in range(last_non_leaf_node,-1,-1):
        heapify(arr,i)

def heapify(arr,i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    n = len(arr)
    if (left < n and arr[left]>arr[largest]):
        largest = left
    if (right< n and arr[right]>arr[largest]):
        largest = right
    if largest != i :
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, largest)




arr = [1,3,5,4,6,13,10,9,8,15,17]

buildHeap(arr)
print(arr)