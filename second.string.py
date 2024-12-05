def compare_strings(str1, str2):
    """
    Compares two strings and determines their equality or difference.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        int: 
            -1 if the second string is larger in size than the first.
             0 if the strings are equal.
             Position (1-indexed) where the first difference is found.
    """
    # Check if the second string is larger
    if len(str2) > len(str1):
        return -1

    # Compare character by character
    for i in range(len(str2)):
        if str1[i] != str2[i]:
            return i + 1  # Return position as 1-indexed

    # Check if the first string has extra characters
    if len(str1) > len(str2):
        return len(str2) + 1

    # Strings are equal
    return 0


# Example usage:
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

result = compare_strings(str1, str2)

if result == -1:
    print("The second string is larger in size than the first string.")
elif result == 0:
    print("The strings are equal.")
else:
    print(f"The strings differ at position {result}.")
