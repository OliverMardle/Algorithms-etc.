names = ['Oliver', 'Colin', 'MrCount','Barry','Python','Jack','Steve','Jake','Dawid']
names.sort()
print(names)
name = input('Enter a name: ')
a = 0
b = len(names)
middle = int((a + b)/2)
tries = 0
while(a != b):
    if name == names[middle]:
        print('[[[True]]]')
        break
    elif name < names[middle]:
        b = middle
        middle = int((a + b)/2)
        tries = tries + 1
    elif name > names[middle]:
        a = middle
        middle = int((a + b)/2)
        tries = tries + 1
    if tries == len(names) - 1:
        print('[[[False]]]')
        break
