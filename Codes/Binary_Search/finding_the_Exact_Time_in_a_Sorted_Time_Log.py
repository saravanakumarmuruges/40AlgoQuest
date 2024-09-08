timestamps = ["00:05", "01:10", "02:20", "03:30", "04:45", "06:00", "07:15", "08:30"]
target = "04:45"
left = 0
right = len(timestamps)


while left<=right:
    mid = (left + right)//2 
    if timestamps[mid] == target:
        print(f"found number {target} in index position {mid}")
        exit()
    elif target < timestamps[mid]:
        right = mid-1
    elif target > timestamps[mid]:
        left = mid+1

print(f"The provided timestamp {target} is not available.")