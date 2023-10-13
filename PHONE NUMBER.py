
'''
---Program 7---
Write a program to find out if the entered phone is valid or not using slicing
'''

count = 0
while True:
    z = input('''The format of the number is
3 digits, a dash, 3 digits, a dash and 4 digits :
(Enter 'y' to continue) ''').strip()
    print("\n")
    if z  == 'y':
       a = input("Enter the phone number according to the format:")
       print("\n")
       if len(a) == 12:
           if a[:3].isdigit():
               if a[3] == '-':
                   if a[4:7].isdigit():
                       if a[7] == '-':
                           if a[8:].isdigit():
                               print("Format is Valid\n")
                           else:
                               print("Third set of characters are invalid\n")
                       elif a[7].isdigit() == False:
                           print(" Second '-' not found. Some other special character found\n")
                       else:
                           print(" Second '-' not found\n")
                   else:
                       print("Second set of characters are invalid\n")
               elif a[3].isdigit() == False:
                    print(" First '-' not found. Some other special character found\n")
               else:
                   print(" First '-' not found\n")
           else:
               print("First set of characters are invalid\n")
       else:
           print("Length of number is wrong\n")
    else:
        print("Exiting now...")
        break
