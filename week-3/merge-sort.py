def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    # Split the list into two halves
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    # Merge sorted halves
    return merge(left, right)

# Recursion
def merge(left, right):
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
