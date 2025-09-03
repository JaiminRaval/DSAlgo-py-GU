# with recursion
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    # Split the list into two halves

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    # Merge sorted halves
    return mergeRecursive(left, right)

# Recursion
def mergeRecursive(left, right):
    result = []
    i, j = 0, 0
    # Compare and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Collect remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example:
print(merge_sort([7, 3, 1, 9, 5, 2]))



# Without recursion
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
            print()
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergeSort(arr):
    step = 1        # Start with smallest subarrays
    length = len(arr)
    while step < length:
        for i in range(0, length, 2 * step):
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]
            merged = merge(left, right)
            # Place the merged part back into arr
            for j, val in enumerate(merged):
                arr[i + j] = val
        step *= 2
    return arr

# Usage example
mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
print(mergeSort(mylist))  # Output: [-13, -10, 3, 6, 7, 15, 23.5, 55]
