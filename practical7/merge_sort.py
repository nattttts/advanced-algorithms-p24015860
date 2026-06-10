# Implement Merge Sort to sort:
# [214, 12, 46, 57, 31, 8]
# Expected Output:
# [8, 12, 31, 46, 57, 214]

merge_sort_list = [214, 12, 46, 57, 31, 8]


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # Append any remaining elements
    result.extend(left)
    result.extend(right)

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


print(merge_sort(merge_sort_list))
