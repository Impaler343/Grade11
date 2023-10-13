
'''
---Program 4---

Write a menu driven program to perform the following

    Menu
    1. Input a string
    2. Palindrome or not
    3. No. of alphabets.
    4. No. of Digits.
    5. Exit
'''

count = summ = 0
while True:
   print('''      Menu
#1 - Input a string
#2 - Palindrome or not
#3 - Number of alphabets
#4 - Number of digits
#5 - Exit\n''')
   a = input("Enter your choice:")
   print("\n")
   if a == '1':
      z = input("Enter the string:")
      print("\n")
   if a == '2':
        new = ''
        for c in z:
           new = c + new
        if new == z:
          print("Palindrome\n")
        else:
          print("Not a palindrome\n")
          new = ''
        continue
   elif a == '3':
        for d in z:
           if d.isalpha():
             count+=1
        print("Number of alphabets:",count,"\n")
        count = 0
        continue
   elif a == '4':
         for d in z:
          if d.isdigit():
            count+=1
         print("Number of digits:",count,"\n")
         count= 0
         continue
   elif a == '5':
       print("Exiting now....")
       break
