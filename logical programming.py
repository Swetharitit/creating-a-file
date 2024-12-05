def is_prime(num):
    # Function to check if a number is prime
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_prime_numbers(start, end):
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")
    print()

# Take input from the user for the range
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

# Call the function to print prime numbers in the given range
print_prime_numbers(start_range, end_range)

