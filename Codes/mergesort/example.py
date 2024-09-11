'''
in = [3,4,1,2]
out = [1,2,3,4]
'''
arr = [3,4,1,2]
def mergesort(arr):
    if len(arr)>1:
        mid = 0 + len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
        left_index=0
        right_index=0
        out_index=0
        while left_index<len(left) and right_index<len(right):
            if left[left_index]<right[right_index]:
                arr[out_index]=left[left_index]
                left_index +=1
            else:
                arr[out_index]=right[right_index]
                right_index +=1
            out_index +=1
        while left_index<len(left):
            arr[out_index]=left[left_index]
            out_index +=1
            left_index +=1
        while right_index<len(right):
            arr[out_index]=right[right_index]
            right_index +=1
            out_index +=1
        return arr

print(mergesort(arr))