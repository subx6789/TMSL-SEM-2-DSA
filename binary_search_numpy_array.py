# Binary Search using Numpy Array Implementation in Python

import numpy as np

def binary_search(arr, k):
    lb, ub = 0, len(arr) - 1
    while lb <= ub:
        mid = (lb + ub) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            lb = mid + 1
        else:
            ub = mid - 1
    return -1

def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

if __name__ == "__main__":
    
    n = int(input("Enter the number of elements in the array: "))
    
    arr = []
    
    print("Enter the elements of the array :- ")
    
    # Taking input and converting to numpy array
    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1} : ")))

    arr = np.array(arr)
    
    # Check if already sorted
    if not np.array_equal(arr, np.sort(arr)):
        insertion_sort(arr)
        print("The sorted array is : ", arr)
    else:
        print("The array is : ", arr)
    
    k = int(input("Enter the element to be searched : "))
    
    result = binary_search(arr, k)
    
    if result != -1:
        print(f"Element {k} found at position number {result + 1}.")
    else:
        print(f"Element {k} not found in the array.")