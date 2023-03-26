# Merging algorithms are a type of sorting algorithm that work by repeatedly merging smaller, 
# sorted arrays into larger, sorted arrays until the entire input array is sorted. 

# The time complexity of Merge Sort is O(n log n), which makes it much more efficient than Selection Sort or Insertion Sort for large datasets. 
# However, Merge Sort has a higher memory overhead than other sorting
# algorithms because it requires creating additional arrays to store the sorted halves during the merging process.


def merging_sort(arr: list[int]) -> list[int]:
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merging_sort(left_half)
        merging_sort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
    return arr


if __name__ == "__main__":
    result = merging_sort([-234, 23, -123, 6, 1, 11, 349, -24423, 1423])
    print(f'RESULT: {result}')
