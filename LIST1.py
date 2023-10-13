
'''
---Program 8---
Write a menu driven program to perform the following :

     Menu
     1. Input a list.
     2. Maximum number and its index
     3. Minimum number and its index.
     4. Count the frequency.
     5. Exit
'''

b  = maxx = minn = ind = count = 0
while True:
    print('''       Menu:
#1 To input list
#2 To find maximum number and its index:
#3 To find minimum number and its index:
#4 To find the frequency of a number:
#5 Exit''')
    print("\n")
    z = input("Enter your choice:")
    print("\n")
    if z == '1':
        a = input("Enter the values separated by a space:").split()
        print("\n")
        z = input("Enter your choice:")
        print("\n")
    if z == '2':
        for c in range(len(a)):
            if int(a[c]) > maxx:
                maxx = int(a[c])
                ind = c
        print("The Maximimum number is", maxx)
        print("Its index value is:", ind,"\n")
        maxx = ind = 0
    elif z == '3':
        minn = int(a[0])
        for c in range(len(a)):
            if int(a[c]) < minn:
                minn = int(a[c])
                ind = c
        print("The Minimum number is", minn)
        print("Its index value is:", ind,"\n")
        minn = ind = 0
    elif z == '4':
        b = int(input("Enter the number to check:"))
        for c in a:
            if int(c) == b:
                count += 1
        print("The frequency of",b,"is:",count,"\n")
        count = 0
    elif z == '5':
        print("Exiting now...")
        break
