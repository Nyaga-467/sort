def counting_sort(arr):
    if not arr:
        return []

    # Step 1: Find the maximum element
    max_element = max(arr)

    # Step 2: Initialize countArray
    count_array = [0] * (max_element + 1)

    # Step 3: Store the count of each unique element
    for num in arr:
        count_array[num] += 1

    # Step 4: Store the cumulative sum
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    # Step 5 and 6: Create output array and place elements at correct positions
    output_array = [0] * len(arr)
    for num in reversed(arr):
        output_array[count_array[num] - 1] = num
        count_array[num] -= 1

    return output_array


# Example usage
input_array = [4, 2, 2, 8, 3, 3, 1]
sorted_array = counting_sort(input_array)
print("Sorted array:", sorted_array)
