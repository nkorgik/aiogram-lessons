# Selection Sort is a simple sorting algorithm that works by repeatedly selecting the smallest element from the unsorted part of 
# the list and swapping it with the element at the beginning of the unsorted part of the list. 
# This process is repeated until the entire list is sorted.

# Selection sorts has the stable time complexity of O(n^2)


def selection_sort(arr: list[int]) -> list[int]:
    length = len(arr) # we avoide multiple calculations
    
    for ix in range(length):
        min_idx = ix
        for jx in range(ix+1, length):
            if arr[jx] < arr[min_idx]:
                min_idx = jx
                
        arr[ix], arr[min_idx] = arr[min_idx], arr[ix]
        
    return arr


if __name__ == "__main__":
    arr = [2, -1, -115, 87, 93]
    print(f'RESULT: {selection_sort(arr)}')
