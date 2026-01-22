# write a program to print given amount into words
# input : 12345 output : one two three four five 
words = ['zero','one','two','three','four','five','six','seven','eight','nine']
#           0     1     2       3       4     5     6       7       8       9    
list=[]
number=int(input("Enter amount:"))
while number>0:
    r=number%10
    list.insert(0,words[r])
    number=number//10
print(' '.join(list))
    
