#iterative binary search
def binary_search(key,arr):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = int((low + high)/2)
        if key == arr[mid]:
            return True
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
