def simple(p,r,n):
    si=p*r*n/100
    return si
p=int(input("Enter principal amount:"))
r=int(input("Enter rate:"))
n=int(input("Enter time"))
res=simple(p,r,n)
print("simple interest is :",res)
