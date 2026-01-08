#write a program to convert given 2 digit amount into words
amount= input("Enetr amount")
amount=int(amount)
last=amount%10
first=amount//10
word=['zero','one','two','three','four','five','six','seven','eight','nine']
print(word[first]," ",word[last])

