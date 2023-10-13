
'''
---Program 5---

Write a menu driven program to perform the following.

     Menu
     1. Input a string
     2. Capitalize each word
     3. No. Of words
     4. Reverse adjacent letters of the word.
     5. Exit
'''


count = 0
summ = 0
b = 0
e = 1
while True:
   print('''      Menu
#1 - Input a string
#2 - Capitalize each word
#3 - Number of Words
#4 - Reverse adjacent letters of a string.
#5 - Exit
\n''')
   a = input("Enter your choice:")
   print("\n")
   if a == '1':
       z = input("Enter the string:").strip()
       print("\n")
       a = input("Enter your choice:")
       print("\n")
   if a == '2':
       new = ''
       new = new + z[0].upper()
       while e < len(z):
            if e <= (len(z)-1) and z[e].isspace() and z[e+1].isalpha():
               new  = new + ' ' +z[e+1].upper()
               e+=2
            else:
               new = new + z[e]
               e+=1
       print("The new string is:",new,"\n")
       z = new
       new = ''
       e = 1
   elif a == '3':
      count = 1
      for e in range(len(z)):
         if e <= (len(z)-1) and z[e].isspace() and z[e+1].isalpha() :
          count+= 1
      print("The number of words are:",count,"\n")
      count = 0
   elif a =='4':
      new = ''
      neww = ''
      m = z.split()
      for c in m:
         if len(c) % 2== 0:
             for d in range(0,len(c),2):
               if d <= len(c)-2:
                 new = new + c[d+1]
                 new = new + c[d]
             if neww == '':
                neww = neww + new
             else:
                neww = neww + ' ' + new
             new = ''
         else:
            for d in range(0,len(c),2):
               if d <= len(c)-2:
                 new = new + c[d+1]
                 new = new + c[d]
            new = new + c[len(c)-1]
            if neww == '':
                neww = neww + new
            else:
                neww = neww + ' ' + new
            new = ''
      print("Reversed string:", neww,"\n")
      z = neww
   elif a == '5':
       print("Exiting now....")
       break
