def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len-1):
        for j in range(arr_len-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    num = input("Enter the list of integers with space between them:\n")
    input_list = num.split()
    int_input_list = list()
    try:
        for i in input_list:
            j = float(i)
            int_input_list.append(j)
    except ValueError:
        print('only numbers allowed')
        exit()
    print(int_input_list)
    output = bubble_sort(int_input_list)
    print(output)

