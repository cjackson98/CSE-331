def merge_sort(unsorted, threshold, reverse):
    """"
    Merge sort. Divides list into 2 new lists, if length of new list(s) is less than
    the threshold, sends them to insertion_sort function to be sorted, otherwise
    loops back to start of merge_sort function and repeats. After lists have been split
    small enough and sorted via insertion_sort, they are combined by being send to
    merge_sort function. If list is small enough (length 1 or less) is is returned rather
    than sorted.
    """
    size = len(unsorted)
    if len(unsorted) <= 1:
        return unsorted
    mid = size // 2
    first = unsorted[0:mid]
    second = unsorted[mid:size]
    if mid > threshold:
        first = merge_sort(first, threshold, reverse)
        second = merge_sort(second, threshold, reverse)
    else:
        first = insertion_sort(first, reverse)
        second = insertion_sort(second, reverse)
    return merge(first, second, reverse)


def merge(first, second, reverse):
    """
    Combines two lists. Order is based on the 'reverse' bool provided. If reverse is true,
    combines the list in descending order. If reverse is false, combines in ascending
    order. Returns combined, sorted list.
    """

    sorted_list = []
    while len(first) != 0 and len(second) != 0:
        if reverse is False:
            if first[0] < second[0]:
                sorted_list.append(first[0])
                first.pop(0)
            else:
                sorted_list.append(second[0])
                second.pop(0)
        else:
            if first[0] > second[0]:
                sorted_list.append(first[0])
                first.pop(0)
            else:
                sorted_list.append(second[0])
                second.pop(0)
    if len(first) == 0:
        sorted_list += second
    else:
        sorted_list += first
    return sorted_list


def insertion_sort(unsorted, reverse):
    """
    Sorts provided list based on 'reverse' bool. If reverse is true, sorts the list
    in descending order. If reverse is false, sorts in ascending order. Sorts via insertion sort.
    """

    size = len(unsorted)
    for i in range(1, size):
        j = i
        if reverse is False:
            while j > 0 and unsorted[j] < unsorted[j-1]:
                temp = unsorted[j]
                unsorted[j] = unsorted[j-1]
                unsorted[j-1] = temp
                j -= 1
        else:
            while j > 0 and unsorted[j] > unsorted[j-1]:
                temp = unsorted[j]
                unsorted[j] = unsorted[j-1]
                unsorted[j-1] = temp
                j -= 1
    return unsorted
