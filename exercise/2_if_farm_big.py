length1=float(input("Enter length of farm1"))
width1=float(input("Enter width of farm1"))
length2=int(input("Enter length of farm2"))
width2=int(input("Enter width of farm2"))
arr1=length1*width1
arr2=length2*width2
if arr1>arr2:
    print("farm 1 is big")
if arr1<arr2:
    print("farm 2 is big")
