
'''
---Program 2---

Write a program to find the sum of the following series:

   x - x²/2! + x³/3! + x^4/4!.... x^n/n!
'''

while True:
    print("\n")
    a = input("Do you want to find the sum of the series?('yes' to proceed)")
    print("\n")
    if a == 'yes':
        x = int(input("Enter the number to use in the sum:"))
        print("\n")
        n = int(input("Enter the number of terms:"))
        print("\n")
        summ = 0
        for c in range(1,n+1):
            prod = 1
            for d in range(1,c+1):
                prod *= d
            if c%2 != 0:
                summ += (x**c)/prod
            else:
                summ -= (x**c)/prod
        print("The sum is:",summ)
    else:
        print("Exiting now...")
        break
