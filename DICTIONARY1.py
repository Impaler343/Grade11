
'''
---Program 16---
Write a menu driven program in python to create, add, delete, search and display dictionary details
'''

d = dict()
while True:
        print('''          Menu
#1 Create dictionary of names and ages
#2 Add a key
#3 Delete a key
#4 Search and Display
#5 Exit''')
        z = input("Enter your choice:")
        print("\n")
        if z == '1':
                l = int(input("Enter the length of the dictionary:"))
                for c in range(l):
                        k = input("Enter user's name: ")
                        v = input("Enter user's age: ")
                        print("\n")
                        d[k] = v
                print("The entered dictionary: ",d,"\n")
        elif z == '2':
                if d == {}:
                        print("Enter the dictionary first...\n")
                        continue
                k = input("Enter user's name: ")
                print("\n")
                v = input("Enter user's age: ")
                d[k]= v
                print("\n")
                print("Updated Dictionary:",d)
        elif z == '3':
                if d == {}:
                        print("Enter the dictionary first...\n")
                        continue
                k = input("Enter the key value to delete:")
                print("\n")
                if k in d:
                        del(d[k])
                        print("Updated Dictionary: ",d,"\n")
                else:
                        print("Name not found\n")
        elif z == '4':
                if d == {}:
                        print("Enter the dictionary first...\n")
                        continue
                k = input("Enter the name to be searched:")
                print("\n")
                if k in d:
                        print("The age: ",d[k],"\n")
                else:
                        print("Name not found\n")
        elif z == '5':
                print("Exiting now...")
                break
