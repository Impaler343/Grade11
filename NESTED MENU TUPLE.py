
'''
---Program 14---
Write a menu program to perform the following operations on a tuple

     Menu
     1. Input a tuple of 3 elements
     2. Unpack and pack the tuple to modify/delete  tuple elements
     3. List constructor method to modify/delete  tuple elements
     4. Exit
'''


while True:
    print('''            Menu
#1 Input a tuple
#2 Unpack and Pack to modify/delete tuple elements
#3 List constructor to modify/delete tuple elements
#4 Exit\n''')
    z = input("Enter your choice:")
    print("\n")
    if z == '1':
        t = ()
        for c in range(3):
            t = t + (input("Enter the names: "),)
    print("\n")
    if z  == '2':
        if t == ():
            print("Enter a tuple first")
            continue
        while True:
            print('''         Sub Menu
#1 Modify
#2 Delete
#3 Exit\n''')
            if len(t) == 3:
                g,h,i = t
            elif len(t) == 2:
                g,h = t
            else:
                 g = t
            y = input("Enter your choice:")
            print("\n")
            if y == '1':
                m = input("Enter the name to be modified:")
                print("\n")
                if m in t:
                    n = input("Enter the new name: ")
                    if g == m:
                        g = n
                    elif h == m:
                        h = n
                    elif i == m:
                        i = n
                    t = g,h,i
                    t = tuple([x for x in t if x])
                    print("The updated tuple: ",t,"\n")
                else:
                    print("The name was not found\n")
            elif y == '2':
                m = input("Enter the name to be deleted:")
                print("\n")
                if m in t:
                    if m == g:
                        g = ''
                    elif m == h:
                        h = ''
                    elif m == i:
                        i = ''
                    t = g,h,i
                    t = tuple([x for x in t if x])
                    print("Updated tuple: ", t,"\n")
                else:
                    print("The name was not found\n")
            elif y == '3':
                print("Exiting loop for modification...\n")
                break
            else:
                print("Enter a valid choice")
    elif z == '3':
        if t == ():
            print("Enter a tuple first")
            continue
        while True:
            l = list(t)
            print('''      Sub Menu
#1 Modify
#2 Delete
#3 Exit''')
            y = input("Enter your choice:")
            print("\n")
            if y == '1':
                m = input("Enter the name to be modified:")
                print("\n")
                if m in l:
                    n = input("Enter the new name: ")
                    for c in range(len(l)):
                        if l[c] == m:
                            l[c] = n
                            t = tuple(l)
                            break
                    print("The updated tuple: ",t,"\n")
                else:
                    print("The name was not found\n")
                    continue
            elif y == '2':
                m = input("Enter the name to be deleted:")
                print("\n")
                if m in l:
                    for c in range(len(l)):
                        if l[c] == m:
                            l.remove(m)
                            t = tuple(l)
                            break
                    print("The updated tuple: ",t,"\n")
                else:
                    print("The name was not found\n")
                    continue
            elif y == '3':
                print("Exiting loop for modification...\n")
                break
            else:
                print("Enter a valid choice")
    elif z == '4':
        print("The final tuple:",t,"\n")
        print("Exiting now....")
        break
