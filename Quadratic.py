import math

def Quadratic():
    # Take inputs for a, b, and c
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the constant c: "))
    
    # Calculate the discriminant (delta)
    delta = b**2 - 4 * a * c
    
    # Check if delta is positive, zero, or negative
    if delta > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"The roots are real and distinct: Root 1 = {root1}, Root 2 = {root2}")
    elif delta == 0:
        # Two real and equal roots
        root = -b / (2 * a)
        print(f"The roots are real and equal: Root = {root}")
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-delta) / (2 * a)
        print(f"The roots are complex: Root 1 = {real_part} + {imaginary_part}i, Root 2 = {real_part} - {imaginary_part}i")

# Run the program
Quadratic()
