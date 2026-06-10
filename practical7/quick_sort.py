# 3. Quick Sort:
# Problem Statement (Please refer to the slides for the Pseudocode)
# Implement Quick Sort to sort:
# [214, 12, 46, 57, 31, 8]
# Expected Output:
# [8, 12, 31, 46, 57, 214]

quick_sort_list = [214, 12, 46, 57, 31, 8]

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def partition(a, first, last):
    # use first item as pivot

    pivot = a[first]
    i = first

    for j in range(first + 1, last + 1):
        if a[j] < pivot:
            i += 1
            swap(a, i, j)

    swap(a, first, i)
    return i


def quick_sort(a, first, last):

    if first < last:
        pivot_index = partition(a, first, last)
        quick_sort(a, first, pivot_index - 1)
        quick_sort(a, pivot_index + 1, last)


quick_sort(quick_sort_list, 0, len(quick_sort_list) - 1)
print(quick_sort_list)