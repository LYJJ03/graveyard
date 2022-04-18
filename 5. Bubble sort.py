def bubble(arr):
    length = len(arr)

    for i in range(length-1):
        for j in range(0,length-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
        
            
