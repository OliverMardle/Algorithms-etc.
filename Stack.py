stack = []
FP = 0

def remove():
    global FP
    OLD = FP
    FP += 1
    if FP > len(stack):
        FP = OLD

def add(x):
    global FP, stack
    stack.insert(FP, x)

choice = input('Press R to remove an entry, A to add an entry, P to look at the current item and X to end the program: ')

while choice != 'x':
    if choice == 'r' or choice == 'R':
        remove()
        print(stack)
        print(stack[FP:])
    if choice == 'a' or choice == 'A':
        item = int(input('Enter a number to add to the stack'))
        add(item)
        print(stack)
        print(stack[FP:])
    choice = input('Press R to remove an entry, A to add an entry, P to look at the current item and X to end the program: ')
        
