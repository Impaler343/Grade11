
'''
---Program 6---
Write a program to add 'ing' to the string if the length of the string is >=3.
If the given string ends with 'ing' then add 'ly' to it.
'''


while True:
    b = input("Do you want to edit your string?('yes' to proceed)")
    print("\n")
    if b == 'yes':
        a = input("Enter a string: ")
        print("\n")
        new = a
        if a[-3:] == 'ing':
            new = new + 'ly'
            print(new,"\n")
        elif len(a) >=3:
            new = new + 'ing'
            print(new,"\n")
        else:
           print("No Alteration\n")
    else:
        print("Exiting now...")
        break
