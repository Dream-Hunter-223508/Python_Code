


def endl():
    print("\n")


def spes():
    print(" ")


def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=" ")
        a,b=b,a+b

        """  #--> same line print()
        temp=a
        a=b
        b=temp+b
        """

fib(2000)
endl()
fib(0)