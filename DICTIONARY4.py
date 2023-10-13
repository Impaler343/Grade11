
'''
---Program 19---
Write a menu driven program to perform the following on dictionary
         Menu
    1.  Create 2 dictionaries
    2. Merge 2 dictionaries
    3. Display common key value pairs
    4. Change the key of the given dictionary
    5. Exit

'''

d = {}
d1 = {}
d1old = {}
dold = {}
while True:
      print('''      Menu
#1 Create 2 dictionaries
#2 Merge 2 dictionaries
#3 Display common key and value
#4 Change key
#5 Exit''')
      z = input("Enter your choice:")
      print("\n")
      if z == '1':
            print("Dictionary 1:\n")
            k = input("Enter keys: ").split()
            print("\n")
            v = [int(val) for val in input("Enter values:").split()]
            d = dict(zip(k,v))
            print("\n")
            print("Dictionary 2:\n")
            k = input("Enter keys: ").split()
            print("\n")
            v = [int(val) for val in input("Enter values:").split()]
            d1 = dict(zip(k,v))
            print("\n")
            print("Dictionary 1:\n",d,"\nDictionary 2:\n",d1,"\n")
      if z == '2':
            dold = d.copy()
            d1old = d1.copy()
            d.update(d1)
            print(d,"\n")
      if z == '3':
          if dold:
           for k,v in dold.items():
                 if k in d1old and v == d1old[k]:
                       print("\t",k,":",v,"\n")
                       break
           else:
                 print("No common key and value\n")
          else:
           for k,v in d.items():
                 if k in d1 and v == d1[k]:
                       print(k,v,"\n")
                       break
           else:
                 print("No common key and value\n")
      if z == '4':
            a = input("Enter 1 to use first dictionary or 2 to use second dictionary:")
            print("\n")
            if a == '1':
                  b = input("Enter the key to change:")
                  print("\n")
                  if b in dold.keys():
                        e = input("Enter the new key:")
                        print("\n")
                        dold[e] = dold[b]
                        del dold[b]
                        print("Updated dictionary:",dold,"\n")
                  else:
                        print("Invalid key\n")
            elif a == '2':
                  b = input("Enter the key to change:")
                  print("\n")
                  if b in d1old.keys():
                        e = input("Enter the new key:")
                        print("\n")
                        d1old[e] = d1old.pop(b)
                        print("Updated dictionary:",d1old,"\n")
                  else:
                        print("Invalid key\n")
      if z == '5':
            print("Exiting now...")
            break
