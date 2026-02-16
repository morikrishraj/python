def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers."
    
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    
    return result


# Taking input
num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
