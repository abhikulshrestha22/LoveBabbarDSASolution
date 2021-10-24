# Problem link https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1

def find(arr, n, x):
    min = -1
    max = -1
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] > x:
            high = mid-1
        elif arr[mid] < x:
            low = mid+1
        else:
            if mid > 0 and x == arr[mid-1]:
                high = mid - 1
            else:
                min = mid
                break
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] > x:
            high = mid-1
        elif arr[mid] < x:
            low = mid+1
        else:
            if mid < len(arr)-1 and x == arr[mid+1]:
                low = mid + 1
            else:
                max = mid
                break
    return [min, max]
