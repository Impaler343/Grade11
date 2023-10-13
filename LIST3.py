
'''
---Program 10---
Write a menu-driven program to perform the following operations on a 2-dimensional list.
         Menu
         1. Create 2D List
         2. Addition
         3. Sum of row elements
         4. Transpose
         5. Exit
'''

while True:
        print('''\n    Menu:
#1 Create 2D List
#2 Addition
#3 Sum of row elements
#4 Transpose
#5 Exit''')
        print("\n")
        z = input("Enter your choice:").strip()
        print("\n")
        if z == '1':
            l = []
            a = int(input("Enter the number of rows: "))
            print("\n")
            for c in range(a):
                l1 = []
                for d in range(a):
                    l1.append(int(input("Enter the values for the first list:")))
                l.append(l1)
            print("\n")
            print("(same number of rows and column as first list)\n")
            m = []
            for c in range(a):
                m1 = []
                for d in range(a):
                    m1.append(int(input('Enter the values for the second list:')))
                m.append(m1)
            print("\n")
            print("First List:\n")
            for i in range(a):
                for j in range(a):
                    print(l[i][j],end='  ')
                print()
            print("\n")
            print("Second List:\n")
            for i in range(a):
                for j in range(a):
                    print(m[i][j],end='  ')
                print()
            print("\n")
        if z == '2':
            n = []
            for c in range(a):
                n1 = []
                for d in range(a):
                    n1.append(l[c][d]+m[c][d])
                n.append(n1)
            for i in range(a):
                for j in range(a):
                    print(n[i][j],end='  ')
                print()
        elif z == '3':
            for c in range(a):
                summ = 0
                for d in range(a):
                    summ += l[c][d]
                print("The sum of the elements of row number(using the first list entered)",c+1,"is:",summ)
        elif z == '4':
            print("Original List:")
            for c in range(a):
                for d in range(a):
                    print(l[c][d],end = '  ')
                print()
            print("Transposed List:")
            for c in range(a):
                for d in range(a):
                    print(l[c][d],end = '  ')
                print()
        elif z == '5':
            print("Exiting now...")
            break
