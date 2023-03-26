# Insertion sort algorithm - This is another simple sorting algorithm that builds the final sorted list one item at a time. 
# It has a time complexity of O(n^2), but can be more efficient than bubble sort for small datasets

# The worst-case time complexity of Insertion Sort is O(n^2), which occurs when the input array is sorted in reverse order.
# In this case, each element has to be compared with every other element in the sorted part of the array, resulting in a quadratic running time.

# However, if the input array is already partially sorted or has a small number of inversions, the running time of Insertion Sort can be much better.
# In fact, for small datasets or partially sorted arrays, Insertion Sort can have a running time that approaches linear time (i.e., O(n)).


def insertion_sort(arr: list[int]) -> list[int]:
    for ix in range(1, len(arr)):
        key = arr[ix]
        j = ix-1
        
        while j>=0 and key<arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
            
    return arr


if __name__ == "__main__":
    print(insertion_sort([3,2,-1,7]))
    