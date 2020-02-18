# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # get smallest value from arr
        min_value = min(arr[i:])
        # get index of smallest value
        min_index = arr.index(min_value)
        # swap
        arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    loop = True
    while loop is True:
        loop = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                loop = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
