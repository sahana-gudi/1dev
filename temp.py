import sys

# If user provides an argument, use it. Otherwise default to 0.
if len(sys.argv) == 2:
    try:
        celsius = float(sys.argv[1])
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        sys.exit(1)
else:
    print("No input given - using default value.")
    celsius = 0

# Convert to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Display results
print("Temperature in Celsius    :", celsius)
print("Temperature in Fahrenheit :", fahrenheit)
print("Final Temperature Conversion Completed")
