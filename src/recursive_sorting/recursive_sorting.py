# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged = []
    left = arrA
    right = arrB

    # while arrA and arrB have data, compare and sort
    while len(left) > 0 and len(right) > 0:
        if arrA[0] > arrB[0]:
            # add smallest value to end of array
            merged.append(arrB[0])
            # remove from original
            arrB.remove(arrB[0])
        else:
            # repeat above, but for arrB
            merged.append(arrA[0])
            arrA.remove(arrA[0])

    while len(left) > 0:
        merged.append(left[0])
        left.remove(left[0])

    while len(right) > 0:
        merged.append(right[0])
        right.remove(right[0])

    return merged


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # split in middle, floor
    split = len(arr) // 2
    # set left and right arrays based on split value
    left = merge_sort(arr[:split])
    right = merge_sort(arr[split:])

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
