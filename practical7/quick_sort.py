# 3. Quick Sort:
# Problem Statement (Please refer to the slides for the Pseudocode)
# Implement Quick Sort to sort:
# [214, 12, 46, 57, 31, 8]
# Expected Output:
# [8, 12, 31, 46, 57, 214]

def swap(x, y):
    temp = x
    x = y
    y = temp


def partition(a, first, last):
    # use first item as pivot

    pivot = a[first]
    current_index = first

    m = first + 1

    while m <= last:
        if a[m] < pivot:
            current_index += 1
            swap(a[m], a[current_index])
        m += 1

    swap(a[first], a[current_index])
    return current_index


def quick_sort(a, first, last):

    if first < last:
        pivot_index = partition(a, first, last)