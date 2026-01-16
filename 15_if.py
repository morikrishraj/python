#find out defernce of perchase price and saleing price   
perchase_price=int(input("enter perchase prisce "))
selling_price=int(input("enter saleing price"))
diffrence=selling_price-perchase_price   
if diffrence>0:
    print("profit  is",diffrence)
if diffrence<0:  
    print("loss is ",diffrence)
if diffrence==0:
    print("No profit No loss")
    
