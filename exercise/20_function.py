#write a program to create function that convert given fahrenheit into celsius

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Example usage
f = float(input("Enter temperature in Fahrenheit: "))
c = fahrenheit_to_celsius(f)
print("Temperature in Celsius:", c)
