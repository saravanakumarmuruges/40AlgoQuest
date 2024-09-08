pages = [1, 10, 25, 37, 45, 56, 67, 78, 89, 99]
target = 45
left = 0
right = len(pages)

while left<=right:
    mid = (left + right)//2 
    if pages[mid] == target:
        print(f"found number {target} in index position {mid}")
    elif target < pages[mid]:
        right = mid-1
    elif target > pages[mid]:
        left = mid+1

print(f"The provided page number {target} is not available.")