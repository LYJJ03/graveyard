#not-in-place quicksort
def quicksort(lst): #chooses the first element as pivot
    if lst == []:
        return lst
    else:
        pivot = lst[0]
        smaller = []
        larger = []

        for item in lst[1:]:
            if item <= pivot:
                smaller.append(item)
            else:
                larger.append(item)
        return quicksort(smaller) + [lst[0]] + quicksort(larger)
