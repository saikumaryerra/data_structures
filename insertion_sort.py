# no imports


def insertion_sort(arr):
    arr_len = len(arr)
    for i in range(1, arr_len):
        key_element = arr[i]
        j = i
        for j in range(i, -1, -1):
            if key_element < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                break
        arr[j] = key_element
    return arr


if __name__ == '__main__':
    num = input("Enter the list of integers with space between them:\n")
    input_list = num.split()
    int_input_list = list()
    try:
        for input_element in input_list:
            list_item = float(input_element)
            int_input_list.append(list_item)
    except ValueError:
        print('only numbers allowed')
        exit()
    print(int_input_list)
    output = insertion_sort(int_input_list)
    print(output)
