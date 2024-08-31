


def endl():
    print("\n")

def spes():
    print(" ")

#--> List  combine means nested LIST
print("................one line code of combine List................... ")
combs=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(combs)
endl()
print("................Multi line code of combine List................... ")
combine=[]
for x in ['a','b','c','d']:
    for y in [1,2,3]:
        if x!=y:
            combine.append((x,y))
print(combine)