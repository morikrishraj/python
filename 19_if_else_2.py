#find out defernce of perchase price and saleing price   
perchase_price=int(input("enter perchase prisce "))
selling_price=int(input("enter saleing price"))
diffrence=selling_price-perchase_price   
if diffrence>0:
    print("profit  is",diffrence)
elif diffrence<0:  
    print("loss is ",diffrence)
else: 
    print("No profit No loss")
    
