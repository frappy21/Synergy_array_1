def sum_negative_between_max_min(array):
    if not array:
        return 0

    max_elem = max(array)
    min_elem = min(array)
    max_index = array.index(max_elem)
    min_index = array.index(min_elem)

    if max_index < min_index:
        start, end = max_index, min_index
    else:
        start, end = min_index, max_index

    negative_sum = sum(x for x in array[start+1:end] if x < 0)

    return negative_sum

input_array = input("Please enter the array elements separated by spaces: ")
A = list(map(int, input_array.split()))
result = sum_negative_between_max_min(A)
print(f"The sum of negative elements between the maximum and minimum elements is: {result}")