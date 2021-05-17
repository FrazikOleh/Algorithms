def insertion_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        for j in range(i + 1):
            if unsorted_list[i] < unsorted_list[j]:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
    return unsorted_list


lst = [5, 4, 2, 6, 3, 8, 1, 7]
print(insertion_sort(lst))
