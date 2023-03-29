# The complexity of counting sort is O(n + k), where n is the length of the input array and k is the range of the input
# (i.e., the difference between the maximum and minimum values).
# In general, counting sort are useful when you have a large input array with a small range or a small number of digits.

def counting_positive_sort(arr):
    """This function is for positive only"""
    max_value = max(arr)
    min_value = min(arr)
    
    count = [0] * (max_value - min_value + 1)
    
    for x in arr:
        count[x-min_value] += 1
    
    sorted_arr = []
    for i in range(len(count)):
        for j in range(count[i]):
            sorted_arr.append(i+min_value)
        
    return sorted_arr


def counting_sort(arr):
    """This if for negative counting sort"""
    shift = abs(min(arr))
    shifted_arr = [x + shift for x in arr]

    max_val = max(shifted_arr)

    count = [0] * (max_val + 1)

    for num in shifted_arr:
        count[num] += 1

    # TODO: should be optimized for complexity O(n+k), think about that =)
    sorted_arr = []
    for i in range(len(count)):
        for j in range(count[i]):
            sorted_arr.append(i - shift)

    return sorted_arr


if __name__ == "__main__":
    arr = [3, 2, 1, 99, 37]
    result = counting_positive_sort(arr)
    print('POSITIVE: ', result, sep='\n')

    my_list = [5, -3, 8, -1, 0, -2, 4]
    sorted_list = counting_sort(my_list)
    print('NEGATIVE: ', sorted_list, sep='\n')
    