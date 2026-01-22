# write a program to print following series 
# 1     -4      9     -16     25      -36     1000
# 1     2       3       4       5       6   
number=1
while number<100:
    s=number*number
    r=number%2
    if r==0:
        s=0-s
    print(s,end=" ")
    number=number+1
