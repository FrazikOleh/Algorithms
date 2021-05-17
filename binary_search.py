import math


def binary_search(list_of_elements, item):
    counter = 0
    start = 0
    end = len(list_of_elements) - 1
    while start <= end:
        counter += 1
        current_position = (end + start) // 2
        if list_of_elements[current_position] == item:
            print('Element', item, 'have index', current_position)
            print('Number of steps:', counter)
            print('The biggest number of steps:', math.ceil(math.log2(len(lst))))
            return current_position
        elif list_of_elements[current_position] < item:
            start = current_position + 1
        else:
            end = current_position - 1
    print("Element wasn't found")
    return None


lst = [i for i in range(0, 100000, 3)]
index1 = binary_search(lst, 15)
print(index1)
index2 = binary_search(lst, 14)
print(index2)
