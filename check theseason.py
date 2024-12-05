def CheckTheSeason():
    # Define seasons based on month numbers
    seasons = {
        (2, 3): "Vasanta",
        (4, 5): "Grishma / Summer",
        (6, 7): "Monsoon / Rainy",
        (8, 9): "Sharada",
        (10, 11): "Hemanta",
        (12, 1): "Shishira / Winter"
    }
    
    # Keep asking for input until a valid month number is entered
    while True:
        try:
            # Get user input
            month = int(input("Enter a month number (1-12): "))
            
            # Check if month is within the valid range
            if month < 1 or month > 12:
                print("Error: Please enter a number between 1 and 12.")
                continue
            
            # Find the season for the entered month
            for months, season in seasons.items():
                if month in months:
                    print(f"The season is: {season}")
                    return  # Exit the loop once a valid month is entered and season is displayed

        except ValueError:
            print("Error: Please enter a valid integer.")

# Run the program
CheckTheSeason()
