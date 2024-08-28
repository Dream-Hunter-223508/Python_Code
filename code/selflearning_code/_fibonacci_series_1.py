

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

#---> other way is a,b=b,a+b ..
endl()

#---> Singel line print system...
print("...........Print Fibo Series in One line...........")
c,d=0,1
while c<1000:
    print(c,end=", ")
    temp2=c
    c=d
    d=c+d
