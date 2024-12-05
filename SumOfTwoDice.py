import random

def sum_of_two_dice():
    """
    Simulates rolling two dice and prints their sum.

    Returns:
        int: The sum of the two dice rolls.
    """
    # Generate two random integers between 1 and 6
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    # Calculate the sum of the two dice
    dice_sum = die1 + die2

    # Print the result
    print(f"Die 1: {die1}, Die 2: {die2}, Sum: {dice_sum}")

    return dice_sum

# Example usage
sum_of_two_dice()
