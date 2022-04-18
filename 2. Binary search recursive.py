#recursive binary search
def binary_search(low, high, key, arr):
    if low > high:
        return False
    else:
        mid = int((low+high)/2)
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            return binary_search(mid + 1, high, key, arr)
        else:
            return binary_search(low, mid - 1, key, arr)
