# write a program to find out which is cheaper product to purchase from 2 product's weight and price. 
# also display how much cheaper per gram 
p1=int(input("Enter price 1:"))
w1=int(input("Enter weight 1"))

p2=int(input("Enter price 2"))
w2=int(input("Enter weight 2"))

if p1<=0 or w1<=0 or p2<=0 or w2<=0:
    print("price and weight is not nagative or zero")
else :
    product1=p1/w1
    product2=p2/w2
    if product1<product2:
        print("1st product is cheaper ",(product2 -product1 ))
    else: 
        print("1st product is cheaper ",(product1 -product2))
    
