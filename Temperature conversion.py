def TemperatureConversion():
    # Ask the user for the temperature unit they want to convert from
    choice = input("Enter 'F' to convert from Fahrenheit to Celsius or 'C' to convert from Celsius to Fahrenheit: ").strip().upper()

    if choice == 'F':
        # Convert Fahrenheit to Celsius
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        
    elif choice == 'C':
        # Convert Celsius to Fahrenheit
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        
    else:
        print("Invalid input. Please enter 'F' or 'C'.")

# Run the program
TemperatureConversion()
