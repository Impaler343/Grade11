
'''
---Program 18---
Write a menu driven program to create a dictionary by tracking the frequency of letters in
          Menu
    1. Frequency of letters in string
    2. Frequency of numbers/chars in list
    3. Exit
'''

while True:
      print('''       Menu
#1 Count in a string
#2 Count in a list
#3 Exit\n''')
      z = input("Enter your choice:")
      print("\n")
      if z == '1':
            string = input("Enter the string:")
            d = {}
            for c in string:
                  if c not in d.keys():
                        d[c] = 1
                  else:
                        d[c] = d[c] +1
            print(d,"\n")
            d = {}
      if z == '2':
            l = input("Enter the list seperated by space:").split()
            print("\n")
            d = {c : l.count(c) for c in l}
            print(d,"\n")
            d = {}
      if z == '3':
            print("Exiting now...")
            break
