global queue1
queue1=[]
global FP
global RP
FP=0
RP=0

def add(x):
    global RP
    RP+=1
    queue1.append(x)

def remove():
#your definition in here
    global FP
    FP += 1
    if FP > RP:
        print('The list is empty')
        FP = RP

choice=input("a to add, r to remove, x to exit: ")
while choice != "x":
    if choice=="a":
        item=input("What to add to the back of the queue?: ")
        add(item)
        print(RP, FP)
    elif choice=="r":
        remove()
        print(RP, FP)

    print(queue1)
    print(queue1[FP:RP])
    choice=input("a to add, r to remove, x to exit: ")

