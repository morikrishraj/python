#write a program to calculate & display count ,total and average of all the numeric value using arbitary argument function 
def getResult(*values):
    count=0
    total=0
    for item in values:
        count=count+1
        total=total+item
        average=total/count
    print(f"count={count},total={total} average={average}")     
getResult(10,20,30,100,200)
