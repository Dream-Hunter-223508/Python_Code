
def endl():
    print("\n")


def spes():
    print(" ")

letter_1=['a','b','c','d','e','f','g']
print(letter_1)
print(letter_1[2:5])
endl()

#-->modify List
print(".............Modifing list...............")
letter_1[1]='B'
print(letter_1)
letter_1[3:]=['D','E','F','G']
print(letter_1)
endl()

#--> Add something in the list........
print("............ADD SOMETING IN LIST.............")
letter_1.append("LIST")
letter_1.append(2024)
print(letter_1)
print("Length of LIST:",len(letter_1))
endl()

#--> Remove item of the list
print("............REMOVE SOMETING IN LIST.............")
letter_1[-1:]=[]
print(letter_1)
print("Length of LIST:",len(letter_1))