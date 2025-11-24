import sys

def readfile(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    arr = list(map(int, lines[1].strip().split(" ")))
    return arr
      

# Merge sort
def mergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    half = n//2
    left = arr[:half]   # split the arr into halves
    right = arr[half:]
    left_division = mergeSort(left) # recursively divide the left half
    right_division = mergeSort(right) # recursively divide the right half
    return merge(left_division, right_division)

def merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right): # within the range of left & right arrays
        if left[i] < right[j]:
            result.append(left[i])  # append the smaller element to the result array
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]  # if len(left) is longer, append remaining elements of left array
    result += right[j:] # if len(right) is longer, append remaining elements of right array 
    return result

# Quick sort
def partition(arr, low, high):
    if len(arr) == 0:
        return []
    pivot = arr[high] # the last element of the array
    i = low-1  # i points to the last element in the arr that < pivot
    for j in range(low, high): # traverse from the first to the last element before the pivot
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
        else:
            continue

    # swap the pivot and arr[i+1](the first number >= pivot)
    arr[i+1],arr[high] = arr[high], arr[i+1]   
    return i+1  # the array index of the pivot

def quickSort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)    # return array index of the pivot
        quickSort(arr,start, p-1)
        quickSort(arr, p+1, end)

# Insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        key_position = i
        for j in range(i-1,-1,-1):
            if arr[j] > key:
                arr[j+1] = arr[j]
                key_position = j
            else:       # if arr[j] <= key, then arr[j-1]... must be <= key
                break
        arr[key_position] = key
    return arr

# python3 Problem1.py ./sort_array/sort_array1.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    arr1 = readfile(filename)
    arr2 = arr1.copy()
    arr3 = arr1.copy()
    print(f"Merge Sort: {mergeSort(arr1)}")

    quickSort(arr2, 0, len(arr2)-1)
    print(f"Quick Sort: {arr2}")
    print(f"Insertion Sort:{insertionSort(arr3)}")


