def find_second_smallest(arr):
    # Remove duplicates by converting to a set and then back to a sorted list
    unique_sorted_arr = sorted(set(arr))
    
    # Check if the array has at least two unique elements
    if len(unique_sorted_arr) < 2:
        return "The array doesn't have a second smallest element."
    
    # The second element in the sorted unique array is the second smallest
    return unique_sorted_arr[1]

# Example usage
array = list(map(int, input("Enter the elements of the array, separated by spaces: ").split()))

# Call the function and print the result
result = find_second_smallest(array)
print("The second smallest element is:", result)
