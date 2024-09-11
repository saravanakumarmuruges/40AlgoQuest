import random
def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = random.choice(arr)
    left = [i for i in arr if i<pivot]
    right =[i for i in arr if i>pivot]
    middle = [i for i in arr if i==pivot]
    return quicksort(left)+middle+quicksort(right)
            

a = [3,4,5,1,2,7,2,5]
print(a)
a = quicksort(a)
print(a)