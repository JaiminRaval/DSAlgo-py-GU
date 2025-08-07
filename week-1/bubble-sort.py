# Bubble Sort BrutForce for our class-1
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original array: ", numbers)
sorted_numbers = bubble_sort(numbers.copy())
print("Sorted array: ", sorted_numbers)


# one another slightly optimized solution:
def bubble_sort_opt(arr, target):

    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []
