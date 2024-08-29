from xml.sax.saxutils import escape


def endl():
    print("\n")


def spes():
    print(" ")

#----> using for loop in string.....
print("..............FOR LOOP IN STRING................")
string1="AMAR"
for i in string1:
    print(i,end=" ")

endl()

#----> using for loop in list.....
print("..............FOR LOOP IN LIST................")
list1=['amr','name','MR.X']
for i in list1:
    print(i,len(i),end=" ")

endl()
print(len(list1))