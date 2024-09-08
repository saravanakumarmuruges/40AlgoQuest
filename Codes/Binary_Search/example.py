arr = [1,2,3,4,5,6,7,8,9,10]
se = 4
left = 0
right = len(arr)


while left<=right:
    mid = (left + right)//2 
    if arr[mid] == se:
        print(f"found number {se} in index position {mid}")
        break
    elif se < arr[mid]:
        right = mid-1
    else:
        left = mid+1