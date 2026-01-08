amount=int(amount)
last=amount%10;
print(last)
middel=(amount//10)%10
print(middel)
first=amount//100
print(first)
word=['zero','one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']

print(word[first]," ")
word=['zero','one','twenty','three hundrty','fourty','fifthty','sixty','seventy','eighty','ninety']
print(word[middel],"")
word=['zero','one','two','three','four','five','six','seven','eight','nine']
print=(word[last],"")
