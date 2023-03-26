# In the average case, Quick Sort has a time complexity of O(n log n), where n is the number of elements in the array.
# This makes Quick Sort a highly efficient sorting algorithm, especially for large datasets.

# One example of the worst-case scenario for Quick Sort is when the pivot element is chosen as the minimum or 
# maximum element in the array


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = quick_sort(arr)
    print("RESULT:", sorted_arr)
