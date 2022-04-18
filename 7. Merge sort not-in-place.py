#not-in-place mergesort
def mergesort(arr):
    length = len(arr)
    if length == 1:
        return arr
    list1 = arr[0:length//2]
    list2 = arr[(length//2):length]

    list1 = mergesort(list1)
    list2 = mergesort(list2)

    return merge(list1, list2)

def merge(arr_1,arr_2): #a,b are arrays
    index_1,index_2,index = 0,0,0
    final = [""]*(len(arr_1)+len(arr_2))
    while index_1 <= len(arr_1)-1 and index_2 <= len(arr_2)-1:
        if arr_1[index_1] > arr_2[index_2]:
            final[index] = arr_2[index_2]
            index += 1
            index_2 += 1
        else:
            final[index] = arr_1[index_1]
            index += 1
            index_1 += 1
    while index_1 <= len(arr_1)-1:
        final[index] = arr_1[index_1]
        index += 1
        index_1 += 1
        
    while index_2 <= len(arr_2)-1:
        final[index] = arr_2[index_2]
        index += 1
        index_2 += 1

    return final
    
