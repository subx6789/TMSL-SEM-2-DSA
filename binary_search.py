# Binary Search Algorithm Implementation in Python 

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
            j-=1

if __name__ == "__main__":
    
    n = int(input("Enter the number of elements in the array: "))
    
    arr = []
    
    print("Enter the elements of the array :- ")
    
    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1} : ")))
    
    if arr != sorted(arr):
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