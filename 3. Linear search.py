#linear search
def linear_search(key, arr):
    for i in range(0,len(arr)):
        if arr[i] == key:
            return True
        else:
            if arr[i] > key:
                return False
    return False
