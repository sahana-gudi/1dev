import sys

# Check if user provided input
if len(sys.argv) == 2:
    celsius = float(sys.argv[1])
else:
    print("No input given - using default value.")
    celsius = 0

# Convert to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Display results
print("Temperature in Celsius    :", celsius)
print("Temperature in Fahrenheit :", fahrenheit)
print("Final Temperature Conversion Completed")
