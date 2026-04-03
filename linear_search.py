# Linear Search Algorithm Implementation in Python 

def linear_search(arr, k):
    for index,value in enumerate(arr):
        if value == k:
            return index
    return -1

if __name__ == "__main__":
    
    n = int(input("Enter the number of elements in the array: "))
    
    arr = []
    
    print("Enter the elements of the array :- ")
    
    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1} : ")))
    
    print("The array is : ", arr)
    
    k = int(input("Enter the element to be searched : "))
    
    result = linear_search(arr, k)
    
    if result != -1:
        print(f"Element {k} found at position number {result + 1}.")
    else:
        print(f"Element {k} not found in the array.")