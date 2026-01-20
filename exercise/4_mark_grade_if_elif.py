sub1=int(input("Enter sub1 mark"))
sub2=int(input("Enter sub2 mark"))
sub3=int(input("Enter sub3 mark"))
sub4=int(input("Enter sub4 mark"))
sub5=int(input("Enter sub5 mark"))
total=sub1+sub2+sub3+sub4+sub5
print(total)
grade=None
per=total/5
if per>=90 and per<100:
    grade='A+'
elif per>=80 and per<89:
    grade='A'
elif per>70 and per<79:
    grade='B'
elif per>60 and per<69:
    grade='C'
elif per>50 and per<59:
    grade='D'
elif per<50:
    print("need to improve")
print("persentage is:",per)
print("grade",grade)
