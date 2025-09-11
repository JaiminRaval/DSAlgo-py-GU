#   Few inportant points:
# Fixed vs Variable Window Sizes
# Common Problem Patterns: Maximum/minimum subarray problems, substring with conditions, finding optimal subarray length, counting valid subarrays, and problems involving consecutive elements or characters.
# solves problems like "max sum of k elements," variable handles "smallest subarray with sum ≥ target."
# Uses left/right pointers to define window boundaries.
# Maintains running calculations (sum, count, frequency map) as window slides


# Below are the code for two types of sliding window:
#   Fixed Window: Maximum sum of k consecutive elements
def max_sum_fixed_window(arr, k):
    if len(arr) < k:
        return -1

    # Calculate first window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide window: remove first, add next
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

#   Variable Window: Smallest subarray with sum >= target
def min_window_sum(arr, target):
    left = 0
    min_length = float('inf')
    current_sum = 0

    for right in range(len(arr)):
        current_sum += arr[right]  # Expand window

        # Contract window while condition is met
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0

# Example usage
arr = [1, 3, 5, 2, 8, 6]
print(f"Max sum of 3 elements: {max_sum_fixed_window(arr, 3)}")  # Output: 16
print(f"Min window for sum >= 10: {min_window_sum(arr, 10)}")    # Output: 2
