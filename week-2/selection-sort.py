#
def selection_sort(arr):

    n = len(arr)
    for i in range(n):

        min_idx = i
        for j in range(i+1, n):

            if arr[j] < arr[min_idx]:
                min_idx = j
        # One of the best way to swap in py (thanks to py)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Example:
nums = [5, 2, 8, 1, 3]
print(selection_sort(nums))
