'''
    write a program to figur outwhether given number is rime or not 
'''
import sys
number=int(input("Enter number"))
divisor=2
while divisor<number:
    reminder=number%divisor
    if reminder==0:
        print("It is not prime number") 
        sys.exit(1)
    else :
        divisor=divisor+1
print("It is prime number")
