
'''
---Program 9---
Write a program to  input an integer list and swap the elements which are multiples of 10 with the element right next to it.
'''

new= []
c  = 0
while True:
    a = input("Enter the values of the list seperated by a space:").split()
    print("\n")
    while c<= len(a) - 1:
        if c <= len(a) - 2 and a[c].isdigit() and int(a[c])%10 == 0:
            new = new + [int(a[c+1])] + [int(a[c])]
            c+=2
        else:
            new.append(int(a[c]))
            c +=1
    print(new',"\n")
    z = input("Enter 'y' to continue:")
    print("\n")
    if z == 'y':
        new = []
        c =  0
        continue
    else:
        print("Exiting now...")
        break
