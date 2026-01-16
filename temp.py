import sys
if len(sys.argv)!=2:
    print("Usage:python temp.py<temp_in_celsius>")
    sys.exit(1)
try:
    celsius=float(sys.argv[1])
    fahrenheit=(celsius*9/5)+32
    print(f"{celsius}°C is equal to {fahrenheit}°F")

except ValueError:
    print ("Plese Enter a valid numeric value for celsius temp")
