

def endl():
    print("\n")

def spes():
    print(" ")


a,b=0,1
while a<10:
    print(a)
    temp=a
    a=b
    b=temp+b
#--> a,b=b,a+b..........this the another solution of line (13-15)
