# Method to take input and form the array
def take_input():
    arr = []
    print("Enter 10 integers:")
    for i in range(10):
        num = int(input(f"Enter number {i+1}: "))
        arr.append(num)
    return arr

# Method to perform Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place, no need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Main program to execute the methods
def main():
    # Take input from the user
    array = take_input()
    
    # Sort the array using bubble sort
    sorted_array = bubble_sort(array)
    
    # Display the sorted array
    print("Sorted array:", sorted_array)

# Run the program
if __name__ == "__main__":
    main()
    
