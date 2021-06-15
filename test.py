import math

def merge_sort(arr):
    n = len(arr)       
    if n > 1 :
        mid = int(math.ceil(n/2))
        left = arr[0:mid]
        right = arr[mid:n]
        # sort the left side
        print(left)
        merge_sort(left)
        # sort the right side
        merge_sort(right)
        # merge the sorted left and right sides together
        merge(left, right, arr)

def merge(left, right, arr):

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
 
        # Checking if any element was left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    # if i == len(left):
    #    set remaining entries in arr to remaining values in right
    # else:
    #    set remaining entries in arr to remaining values in left
x = [38, 27, 43, 3, 9, 82, 10]
merge_sort(x)
print(x)