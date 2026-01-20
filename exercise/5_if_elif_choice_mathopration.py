num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
print("1.addition,2.subtraction,3.multiplication,4.divison")
choice=int(input("Enter your choice"))

if choice==1:
    print("addition is: ",num1+num2)
elif choice==2:
    print("subtraction is:",num1-num2)
elif choice==3:
    print("multiplication is:",num1*num2)
elif choice==4:
    print("divison is:",num1/num2)
else: 
    print("invalid choice ")
