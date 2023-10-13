
'''
---Program 13---
Write a menu program to store student information in a tuple and perform the following operation.

     Menu
     1. Input student information.
     2. Display student wise total marks and average
     3. Display the ranking  list and details of maximum mark
     4. Exit
'''

maxs = '' 
maxx = 0
first = 0
fp = ''
second = 0
sp = ''
third = 0
tp = ''
while True:
    print('''           Menu
#1 Input  Name, Roll number and Marks for 3 students
#2 Calculating and displaying the sum and Average of marks
#3 Display the Rank of Students
#4 Exit''')
    z = input("Enter your choice:")
    print("\n")
    if z == '1':
        t  = ()
        for c in range(3):
            print("Student",c+1,"\n")
            m = (input("Enter your name:"),) , (int(input("Enter you roll number:")),) , ((int(input("Enter your marks in Physics:"))) , (int(input("Enter your marks in Chemistry:"))) , (int(input("Enter your marks in Math:"))) )
            print("\n")
            t = t + (m,)
        print("Name\t\tRoll Number\t\t  Marks")
        for c in range(3):
            print(str(t[c][0][0]),end = '\t\t    ')
            print(t[c][1][0],end = '\t\t\t')
            for d in range(3):
               print(t[c][2][d], end = '  ')
            print("\n")
        print("\n")
    if z == '2':
        if  t == ():
            print("Enter the details first...")
            continue
        for c in range(3):
            print("Student Name: ", t[c][0][0])
            print("Total Marks: ", t[c][2][0] + t[c][2][1] + t[c][2][2])
            print("Average: ", round(((t[c][2][0] + t[c][2][1] + t[c][2][2])/3),2))
            print("\n")
    if z == '3':
        if  t == ():
            print("Enter the details first...")
            continue
        sum1 = t[0][2][0] + t[0][2][1] + t[0][2][2]
        sum2 = t[1][2][0] + t[1][2][1] + t[1][2][2]
        sum3 = t[2][2][0] + t[2][2][1] + t[2][2][2]
        tt = sum1,sum2,sum3
        first = max(tt)
        tt = tt[:tt.index(max(tt))] + tt[tt.index(max(tt))+1:]
        third = min(tt)
        tt = tt[:tt.index(min(tt))] + tt[tt.index(min(tt))+1:]
        second = tt[0]
        if first == sum1:
            fp = t[0][0][0]
        elif first == sum2:
            fp = t[1][0][0]
        else:
            fp = t[2][0][0]
        if second == sum1:
            sp = t[0][0][0]
        elif second == sum2:
            sp = t[1][0][0]
        else:
            sp = t[2][0][0]
        if third == sum1:
            tp = t[0][0][0]
        elif third == sum2:
            tp = t[1][0][0]
        else:
            tp = t[2][0][0]
        for c in range(3):
            if max(t[c][2]) >= maxx:
                maxx = max(t[c][2])
                maxp = t[c][0][0]
                if maxx == t[c][2][0]:
                    maxs = 'Physics'
                elif maxx == t[c][2][1]:
                    maxs = 'Chemistry'
                else:
                    maxs = 'Math'
        print("Rank 1:",fp,"-",first,"marks")
        print("Rank 2:",sp,"-",second,"marks")
        print("Rank 3:",tp,"-",third,"marks")
        print("\n")
        print("Maximum marks scored:",maxx,"by",maxp,"in",maxs)
        print("\n")
    if z == '4':
        print("Exiting Now...")
        break
