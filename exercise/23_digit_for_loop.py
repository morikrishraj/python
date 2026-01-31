text=input("Enter String:")
count=0
for ch in text:
    if ch.isdigit():
        count+=1
print("digit  in string:",count)  