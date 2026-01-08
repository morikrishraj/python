amount=input("Enter amount")
amount=int(amount)
last=amount%10;
print(last)
middel=(amount//10)%10
print(middel)
first=amount//100
print(first)
word=['zero','one','two','three','four','five','six','seven','eight','nine']
print(word[first]," ",word[middel]," ",word[last])