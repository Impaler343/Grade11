
'''
---Program 11---
Write a  nested menu program to insert single/multiple elements into a list

     Menu
     1. Input a list
     2. Insert elements in the list
        1. Single Element
           1. Add in the middle
           2. Add at the end
           3. Exit
        2. Multiple Elements
           1. Add in the middle
           2. Add at the end
           3. Exit
        3. Exit
     3. Exit
'''

o = []
while True:
    print('''        Menu:
#1 Input list
#2 Insert elements in the list
#3 Exit\n''')
    z = input("Enter your choice:")
    print("\n")
    if z == '1':
        a = []
        a = [int(i) for i in input("Enter the elements of the list seperated by a space:").split()]
        print("\n")
        print("The list that you entered:", a)
        print("\n")
    if z == '2':
        if a == []:
            print("Enter a list first:\n")
            continue
        else:
            while True:
                print('''        Menu:
#1 Single Element
#2 Multiple elements
#3 Exit\n''')
                x = input("Enter your choice:")
                print("\n")
                if x == '1':
                    while True:
                        print('''        Menu:
#1 Add in the middle
#2 Add at the end
#3 Exit\n''')
                        w = input("Enter your choice:")
                        if w!= '3':
                            m = int(input("Enter the number to add:"))
                        else:
                            pass
                        if w == '1':
                            n = int(input("Enter the index(position):"))
                            a = a[:n] + [m] + a[n:]
                            print("The updated list:",a,"\n")
                        elif w == '2':
                            a.append(m)
                            print("The updated list:",a,"\n")
                        elif w == '3':
                            print("\n")
                            print('''Exiting loop for addition of elements
and moving to number of elements loop...\n''')
                            break
                if x == '2':
                    while True:
                        print('''        Menu:
#1 Add in the middle
#2 Add at the end
#3 Exit\n''')
                        w = input("Enter your choice:")
                        if w!= '3':
                            h = input("Enter the numbers to add seperated by space:").split()
                            for i in range(len(h)):
                                o.append(int(h[i]))
                        else:
                            pass
                        if w == '1':
                            n = int(input("Enter the index(position):"))
                            a = a[:n] + o + a[n:]
                            o = []
                            print("The updated list:",a,"\n")
                        if w == '2':
                            a.extend(o)
                            print("The updated list:",a,"\n")
                        if w == '3':
                            print("\n")
                            print('''Exiting loop for addition of elements
and moving to number of elements loop...\n''')
                            break
                if x == '3':
                    print("Exiting loop for inserting elements...\n")
                    break
    if z == '3':
        print("Exiting now...\n")
        break
print("Program over")
