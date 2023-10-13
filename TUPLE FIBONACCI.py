
'''
---Program 12---
Write a menu program to perform the following on tuple

     Menu
     1. Create the Fibonacci series
     2. Identify the value for the given index
     3. Identify the index for the given value
     4. Exit
'''


while True:
    print('''        Menu
#1 Create a Fibonacci series
#2 Identify the value for the given index
#3 Identify the index for the given value
#4 Exit''')
    z = input("Enter your choice:")
    print("\n")
    if z == '1':
        a = int(input("Enter the number of elements of the series to be displayed: "))
        t = (0,)
        n = 0
        o = 1
        d = 0
        for c in range(a):
            d  = n+o
            t = t + (d,)
            o = n
            n = d
        print("The tuple:",t,"\n")
    if z == '2':
            try:
                x = int(input("Enter the index value:"))
                print("\n")
                print("The number:",t[x],"\n")
            except:
                print("Index out of Range\n")
    if z == '3':
            try:
                x = int(input("Enter the digit:"))
                print("\n")
                print("The index value: ",t.index(x),"\n")
            except:
                print("The number was not found\n")
    if z == '4':
        print("Exiting now...")
        break
