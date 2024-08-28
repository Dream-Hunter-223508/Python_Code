

def endl():
    print("\n")

def spes():
    print(" ")


a,b=0,1
while a<10:
    print(a)
    temp1=a
    a=b
    b=temp1+b
#--> a,b=b,a+b..........this the another solution of line (13-15)
endl()
print("............Serial line print:..........")
c,d=0,1
while c<1000:
    print(c,end=',')
    temp2=c
    c=d
    d=temp2+d

