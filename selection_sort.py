def selection_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        smallest = unsorted_list[i]
        index_smallest = i
        for j in range(i, n):
            if unsorted_list[j] < smallest:
                smallest = unsorted_list[j]
                index_smallest = j
        unsorted_list[index_smallest], unsorted_list[i] = unsorted_list[i], unsorted_list[index_smallest]
    return unsorted_list


lst = [5, 4, 2, 6, 3, 8, 1, 7]
print(selection_sort(lst))
