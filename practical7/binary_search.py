# 4. Binary Search:
# Problems Statement (Please refer to the slides for the Pseudocode)
# Using Binary Search, find:
# 31
# in:
# [8, 12, 31, 46, 57, 214]
# Return the index.
# Expected Output:
# Found at index 2

def binary_search(arr, target):
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

    return -1  # not found


binary_search_list = [8, 12, 31, 46, 57, 214]
target_no = 31

result = binary_search(binary_search_list, target_no)
print("Found at index", result)