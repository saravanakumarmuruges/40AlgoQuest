'''
arr = [1, 2, 3, 4, 6,1,4,6]
target = 12
'''
arr = [1, 2, 3, 4, 6,1,4,6]
target = 12
def two_pointer(arr, target):
    l=0
    h=len(arr)-1
    while l<h:
        # print((arr[l]+ arr[h]))
        if arr[l]+arr[h]==target:
            return (arr[l], arr[h])
        elif (arr[l]+arr[h])<target:
            l+=1
        else:
            h-=1

print(two_pointer(arr, target))