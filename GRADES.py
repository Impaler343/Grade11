
'''
---Program 1---

Write a program to display the grade for a given mark using if else statements

'''

while True:
    try:
        a = int(input("Enter your marks out of 100:(or 'exit' to Exit)"))
        if a >=90:
            print("Grade: A")
        elif a>=80:
            print("Grade: B")
        elif a>=70:
            print("Grade: C")
        elif a>=60:
            print("Grade: D")
        elif a>=50:
            print("Grade: E")
        else:
            print("You Failed...")
        print("\n")
    except:
        print("\nExiting now...")
        break
