arr = [2,4,6,8,1,3,5,7]

def cyclic_sort(arr):
    i=0
    while i <len(arr):
        new_index = arr[i] -1
        if arr[i] != arr[new_index]:
            arr[new_index], arr[i] = arr[i], arr[new_index]
        else:
            i+=1
    return arr

print(cyclic_sort(arr))