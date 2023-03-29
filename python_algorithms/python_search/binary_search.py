# Binary search is an algorithm used for searching a sorted array or list. 
# It works by repeatedly dividing the search interval in half until the target value is found or the interval is empty.

# Binary search is a very efficient algorithm, with a time complexity of O(log n), where n is the size of the array. 
# It is much faster than linear search, which has a time complexity of O(n) in the worst case.

def binary_search(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1 # not found


arr1 = [1, 2, 3, 4, 5]
target1 = 3
assert binary_search(arr1, target1) == 2

arr2 = [10, 20, 30, 40, 50, 60]
target2 = 50
assert binary_search(arr2, target2) == 4

arr3 = [1, 3, 5, 7, 9, 11]
target3 = 4
assert binary_search(arr3, target3) == -1

arr4 = []
target4 = 10
assert binary_search(arr4, target4) == -1

arr5 = [1, 2, 2, 2, 3, 4]
target5 = 2
assert binary_search(arr5, target5) == 2

