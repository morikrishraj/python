# write a program to convert 24 hours time into 12 hours format time and display it with AM PM message. 
time=int(input("Enter the time from 1 to 24:"))
am='am'
pm='pm'
if time >12 and time<=24 :
    print("time in hours is:",time-12,"",pm)
if time<=12 :
    print("time in hours is:",time,"",pm)
if time>24: 
    print("invalid time")
